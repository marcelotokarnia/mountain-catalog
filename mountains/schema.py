import graphene
import graphql_geojson
from mountains.models import Mountain
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry
from graphene_django.converter import convert_django_field

@convert_django_field.register(Distance)
def my_convert_function(field, registry=None):
    return field.km


class MountainType(graphql_geojson.GeoJSONType):
    distance = graphene.Float()
    class Meta:
        model = Mountain
        geojson_field = 'spot'


class Query(object):
    mountains = graphene.List(
        MountainType,
        distance=graphene.Int(),
        lat=graphene.Float(),
        lng=graphene.Float()
    )

    def resolve_mountains(self, info, **args):
        distance = args.get('distance')
        lat = args.get('lat')
        lng = args.get('lng')
        pnt = GEOSGeometry('POINT(%.6f %.6f)' % (lat, lng), srid=4326)
        queryset = Mountain.objects.filter(
            spot__distance_lte=(pnt, D(km=distance))
        ).annotate(distance=Distance('spot', pnt))
        for mount in queryset:
            mount.distance = mount.distance.km
        return queryset
