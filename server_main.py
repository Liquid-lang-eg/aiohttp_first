from aiohttp import web
from dotenv import load_dotenv
import os

load_dotenv()

routes = web.RouteTableDef()

resources = dict()
resources[1] = 'https://openai.com/'
resources[2] = 'https://github.com/'


@routes.get('/api/resources')
async def get_all_resources(request):
    if resources:
        return web.json_response([{"id": id, "name": name} for id, name in resources.items()], status=200)
    return web.Response(
        text='Contains no data',
        status=200
    )


@routes.post('/api/resources')
async def create_resource(request):
    client_request = await request.json()
    new_id = max(resources.keys(), default=0) + 1
    resource_value = client_request.get("name")
    if not resource_value:
        return web.Response(
            text='Request must contain a "name" key',
            status=400
        )
    resources[new_id] = resource_value

    return web.Response(
        text="Resource was added",
        status=201
    )


@routes.get('/api/resource/{id}')
async def get_resource(request):
    resource_id = int(request.match_info["id"])
    for id in resources.keys():
        if id == resource_id:
            content = resources[id]
            return web.Response(
                text=content,
                status=200
            )
    return web.Response(
        text='content not found',
        status=404
    )


@routes.delete('/api/resource/{id}')
async def delete_resource(request):
    resource_id = int(request.match_info['id'])
    for id in resources.keys():
        if resource_id == id:
            del resources[resource_id]
            return web.Response(
                text=f'resource with id {resource_id} was deleted',
                status=202
            )
    return web.Response(
        text="the resource was not found",
        status=404
    )


app = web.Application()
app.add_routes(routes)
if __name__ == '__main__':
    web.run_app(app, host=os.environ['ALLOWED_HOST'], port=8000)