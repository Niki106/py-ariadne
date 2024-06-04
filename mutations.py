from ariadne import ObjectType, convert_kwargs_to_snake_case

from store import users, blogs

mutation = ObjectType("Mutation")


@mutation.field("createUser")
@convert_kwargs_to_snake_case
async def resolve_create_user(obj, info, username, email, password):
    try:
        if not users.get(username):
            user = {
                "id": len(users) + 1,
                "email": email,
                "password": password,
            }
            users[username] = user
            return {
                "success": True,
                "user": user
            }
        return {
            "success": False,
            "errors": ["Username is taken"]
        }

    except Exception as error:
        return {
            "success": False,
            "errors": [str(error)]
        }

@mutation.field("createblog")
@convert_kwargs_to_snake_case
async def resolve_create_blog(obj, info, content, title, description, completed, ownerId):
    try:
        blog = {
            "ID": id,
            "title": title,
            "description": description,
            "completed": completed,
            "ownerId": ownerId
        }
        blogs.append(blog)
        return {
            "success": True,
            "blog": blog
        }
    except Exception as error:
        return {
            "success": False,
            "errors": [str(error)]
        }