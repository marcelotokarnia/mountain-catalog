import graphene
from mountains.models import Mountain
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry
from utils.schema_utils import find_operation_field, get_selections


class ActivityType(graphene.ObjectType):
    """ Strava Activity representation """
    id = graphene.ID()
    # distance = graphene.Float(description="Distance from given position on query")
    # position = graphene.Field(PositionType, description="Mountain peak geo point")
    # elevation = graphene.Int(description="Mountain height in meters")
    # name = graphene.String()
    # country = graphene.String()
    # image = graphene.String()
    # province = graphene.String()
    # state = graphene.String()
    # curiosities = graphene.String()
    # region = graphene.String()
    # created_by = graphene.String()


class Query(graphene.ObjectType):
    activities = graphene.List(
        ActivityType,
        description="Query strava activities"
    )

    def resolve_activities(self, info, **args):
        # distance = args.get('distance')
        # elevation = args.get('elevation')
        # position = args.get('position')
        # sort = args.get('sort')

        # selections = get_selections(
        #     find_operation_field(info.field_asts, 'mountains'),
        #     info.fragments
        # )

        # queryset = Mountain.objects.all()
        # if elevation is not None:
        #     if elevation.min is not None:
        #         queryset = queryset.filter(
        #             elevation__gte=elevation.min
        #         )
        #     if elevation.max is not None:
        #         queryset = queryset.filter(
        #             elevation__lte=elevation.max
        #         )
        # if position is not None:
        #     pnt = position.point
        #     if distance is not None:
        #         if distance.max is not None:
        #             queryset = queryset.filter(
        #                 spot__distance_lte=(pnt, D(km=distance.max))
        #             )
        #         if distance.min is not None:
        #             queryset = queryset.filter(
        #                 spot__distance_gte=(pnt, D(km=distance.min))
        #             )
        #     queryset = queryset.annotate(distance=Distance('spot', pnt))
        results = []
        # for mount in queryset:
        #     results.append(MountainType(mount, selections))
        return results
