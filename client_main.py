from aiohttp import client
import asyncio
from dotenv import load_dotenv

load_dotenv()


async def get_all_resources():
    async with client.ClientSession() as session:
        url = 'http://127.0.0.1:8000/api/resources'
        async with session.get(url) as responce:
            text, status_code = await responce.text(), responce.status
            print(f'GET Response: {text}, status code: {status_code}')


async def post_new_resource(resource_name: str):
    data = {"name": resource_name}
    async with client.ClientSession() as session:
        url = "http://127.0.0.1:8000/api/resources"
        async with session.post(url, json=data) as response:
            text, status_code = await response.text(), response.status
            print(f'POST new({resource_name}) Response: {text}, status code: {status_code}')


async def get_url_by_id(resource_id: str):
    async with client.ClientSession() as session:
        url = f"http://127.0.0.1:8000/api/resource/" + resource_id
        async with session.get(url) as response:
            text, status_code = await response.text(), response.status
            print(f'GET by id Response: {text}, status code: {status_code}')


async def delete_by_id(resource_id: str):
    async with client.ClientSession() as session:
        url = f"http://127.0.0.1:8000/api/resource/" + resource_id
        async with session.delete(url) as response:
            text, status_code = await response.text(), response.status
            print(f'DELETE by id({resource_id}) Response: {text}, status code: {status_code}')


async def main():
    await asyncio.gather(
        get_all_resources(),
        post_new_resource('https://www.youtube.com/'),
        get_url_by_id('1'),
        get_url_by_id('0'),
        delete_by_id('2'),

    )


if __name__ == '__main__':
    asyncio.run(main())