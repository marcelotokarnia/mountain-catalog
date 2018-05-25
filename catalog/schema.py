import json
import graphene
from django.contrib.gis.db import models
from graphene_django.converter import convert_django_field
import mountains.schema


class Query(mountains.schema.Query, graphene.ObjectType):
  # This class extends all abstract apps level Queries and graphene.ObjectType
  pass

schema = graphene.Schema(query=Query)
