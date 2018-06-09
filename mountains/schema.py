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
        lng=graphene.Float(),
        elevation=graphene.Int(),
    )

    def resolve_mountains(self, info, **args):
        distance = args.get('distance')
        elevation = args.get('elevation')
        lat = args.get('lat')
        lng = args.get('lng')
        queryset = Mountain.objects.all()
        if elevation is not None:
            queryset = queryset.filter(
                elevation__gte=elevation
            )
        if lat is not None and lng is not None:
            pnt = GEOSGeometry('POINT(%.6f %.6f)' % (lat, lng), srid=4326)
            if distance is not None:
                queryset = queryset.filter(
                    spot__distance_lte=(pnt, D(km=distance))
                )
            queryset = queryset.annotate(distance=Distance('spot', pnt))
        results = []
        for mount in queryset:
            if hasattr(mount, 'distance'):
                mount.distance = mount.distance.km
            results.append(mount)
        return results
