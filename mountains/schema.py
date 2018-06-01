import graphene
import graphql_geojson
from mountains.models import Mountain


class MountainType(graphql_geojson.GeoJSONType):
    class Meta:
        model = Mountain
        geojson_field = 'spot'


class Query(graphene.AbstractType):
    mountains = graphene.List(MountainType)

    def resolve_mountains(self, info):
        return Mountain.objects.all()
