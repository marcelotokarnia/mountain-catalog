import graphene
from mountains.models import Mountain
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry
from graphene_django.converter import convert_django_field

@convert_django_field.register(Distance)
def my_convert_function(field, registry=None):
    return field.km


class MountainType(graphene.ObjectType):
    distance = graphene.Float()
    lat = graphene.Float()
    lng = graphene.Float()
    elevation = graphene.Int()
    name = graphene.String()
    def __init__(self, mountain):
        if hasattr(mountain, 'distance'):
            self.distance = float('%.2f' % mountain.distance.km)
        self.lat = mountain.spot.x
        self.lng = mountain.spot.y
        self.name = mountain.name
        self.elevation = mountain.elevation


class SortingOptions(graphene.InputObjectType):
    param = graphene.String()
    reverse = graphene.Boolean()


class MinMaxInt(graphene.InputObjectType):
    min = graphene.Int()
    max = graphene.Int()


class Position(graphene.InputObjectType):
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
        sort=SortingOptions()
    )

    def resolve_mountains(self, info, **args):
        distance = args.get('distance')
        elevation = args.get('elevation')
        position = args.get('position')
        sort = args.get('sort')

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
            results.append(MountainType(mount))
        return results
