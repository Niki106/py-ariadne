from ariadne import SubscriptionType, convert_kwargs_to_snake_case
from graphql.type import GraphQLResolveInfo

subscription = SubscriptionType()


@convert_kwargs_to_snake_case
@subscription.field("reviewblog")
async def review_blog_resolver(review_blog, info: GraphQLResolveInfo, token: str):
    return {"id": review_blog}