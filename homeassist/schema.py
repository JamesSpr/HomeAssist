import graphene
import kitchen.schema
import lights.schema


class Query(
    kitchen.schema.Query,
    lights.schema.Query,
    graphene.ObjectType
):
    pass

class Mutation(
    kitchen.schema.Mutation,
    lights.schema.Mutation,
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)