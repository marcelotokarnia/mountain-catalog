import graphene
import graphql_geojson
from mountains.models import Mountain
from django.contrib.gis.measure import D
from django.contrib.gis.geos import GEOSGeometry



class MountainType(graphql_geojson.GeoJSONType):
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
        print('POINT(%.6f %.6f)' % (lat, lng))
        pnt = GEOSGeometry('POINT(%.6f %.6f)' % (lat, lng), srid=4326)
        print(Mountain.objects.filter(spot__distance_lte=(pnt, D(km=distance))).count())
        return Mountain.objects.filter(spot__distance_lte=(pnt, D(km=distance)))
