import graphene


class UserType(graphene.ObjectType):
    """ User representation """
    username = graphene.String(description="User primary key")

    def __init__(self, context_user):
        self.username = context_user.username


class Query(graphene.ObjectType):
    user = graphene.Field(
        UserType,
        description="Get logged user information"
    )

    def resolve_user(self, info, **args):
        if info.context.user.is_anonymous:
            return None
        return UserType(info.context.user)
