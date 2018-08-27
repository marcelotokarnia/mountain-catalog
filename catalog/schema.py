import graphene
import mountains.schema
import core.schema


class Query(core.schema.Query, mountains.schema.Query, graphene.ObjectType):
    """Through the following queries you can easily fetch data from the database"""
    pass


schema = graphene.Schema(query=Query)
