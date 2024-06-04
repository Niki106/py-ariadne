from typing import Optional

from ariadne import QueryType, convert_kwargs_to_snake_case

from crud import get_blogs, get_blog # Create a file called crud.py and add the get_blogs function
from schemas.error import MyGraphQLError


@convert_kwargs_to_snake_case
async def resolve_blogs(obj, info, skip: Optional[int] = 0, limit: Optional[int] = 100):
    blogs = await get_blogs(skip=skip, limit=limit)

    return {"blogs": blogs}


@convert_kwargs_to_snake_case
async def resolve_blog(obj, info, blog_id):
    blog = await get_blog(blog_id=blog_id)

    if not blog:
        raise MyGraphQLError(code=404, message=f"blog id {blog_id} not found")

    return {"success": True, "blog": blog}


query = QueryType()
query.set_field("blogs", resolve_blogs)
query.set_field("blog", resolve_blog)