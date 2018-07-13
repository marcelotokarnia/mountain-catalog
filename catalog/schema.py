import graphene
import mountains.schema


class Query(mountains.schema.Query, graphene.ObjectType):
    """Through the following queries you can easily fetch data from the database"""
    pass


schema = graphene.Schema(query=Query)
