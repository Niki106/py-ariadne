from mutations import mutation
from ariadne import QueryType, make_executable_schema, load_schema_from_path
from ariadne.asgi import GraphQL

type_defs = load_schema_from_path("schema.graphql")

query = QueryType()


schema = make_executable_schema(type_defs, query, mutation)
app = GraphQL(schema, debug=True)