import graphene
from mountains.models import Mountain
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry
from utils.schema_utils import find_operation_field, get_selections


class PositionType(graphene.ObjectType):
    """ GeoLocation Point type """
    lat = graphene.Float()
    lng = graphene.Float()

    def __init__(self, point):
        if point:
            self.lat = point.x
            self.lng = point.y


class MountainType(graphene.ObjectType):
    """ Mountain representation """
    id = graphene.ID()
    distance = graphene.Float(description="Distance from given position on query")
    position = graphene.Field(PositionType, description="Mountain peak geo point")
    elevation = graphene.Int(description="Mountain height in meters")
    name = graphene.String()
    country = graphene.String()
    image = graphene.String()

    def __init__(self, mountain, selections):
        if hasattr(mountain, 'distance'):
            self.distance = float('%.2f' % mountain.distance.km)
        else:
            self.distance = None
        self.position = PositionType(mountain.spot)
        self.name = mountain.name
        self.elevation = mountain.elevation
        self.country = mountain.country
        self.id = mountain.id
        if 'image' in selections:
            imageRecord = mountain.images.order_by('-votes').first()
            if imageRecord:
                self.image = imageRecord.image.url
            else:
                self.image = None
        else:
            self.image = None


class SortingOptions(graphene.InputObjectType):
    """ Sorting options type input """
    param = graphene.String()
    reverse = graphene.Boolean()


class MinMaxInt(graphene.InputObjectType):
    """ Range type input """
    min = graphene.Int()
    max = graphene.Int()


class Position(graphene.InputObjectType):
    """ GeoLocation Point type input """
    lat = graphene.Float()
    lng = graphene.Float()

    @property
    def point(self):
        return GEOSGeometry('POINT(%.6f %.6f)' % (self.lat, self.lng), srid=4326)


class Query(graphene.ObjectType):
    mountains = graphene.List(
        MountainType,
        distance=MinMaxInt(),
        position=Position(),
        elevation=MinMaxInt(),
        sort=SortingOptions(),
        description="Query mountains by distance or elevation"
    )

    mountain = graphene.Field(
        MountainType,
        id=graphene.String(),
        position=Position(),
        description="Detailed query a mountain with given ID"
    )

    def resolve_mountain(self, info, **args):
        mountain_id = args.get('id')
        position = args.get('position')
        selections = get_selections(
            find_operation_field(info.field_asts, 'mountain'),
            info.fragments
        )

        queryset = Mountain.objects.filter(pk=mountain_id)
        if position is not None:
            pnt = position.point
            queryset = queryset.annotate(distance=Distance('spot', pnt))
        mount = queryset.first()
        if mount:
            return MountainType(mount, selections)
        else:
            return None

    def resolve_mountains(self, info, **args):
        distance = args.get('distance')
        elevation = args.get('elevation')
        position = args.get('position')
        sort = args.get('sort')

        selections = get_selections(
            find_operation_field(info.field_asts, 'mountains'),
            info.fragments
        )

        queryset = Mountain.objects.all()
        if elevation is not None:
            if elevation.min is not None:
                queryset = queryset.filter(
                    elevation__gte=elevation.min
                )
            if elevation.max is not None:
                queryset = queryset.filter(
                    elevation__lte=elevation.max
                )
        if position is not None:
            pnt = position.point
            if distance is not None:
                if distance.max is not None:
                    queryset = queryset.filter(
                        spot__distance_lte=(pnt, D(km=distance.max))
                    )
                if distance.min is not None:
                    queryset = queryset.filter(
                        spot__distance_gte=(pnt, D(km=distance.min))
                    )
            queryset = queryset.annotate(distance=Distance('spot', pnt))
        results = []
        for mount in queryset:
            results.append(MountainType(mount, selections))
        return results
