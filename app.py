import asyncio
import random

from aiohttp import web, Response
from aiohttp.web_reqrep import Request

async def test_route(request: Request) -> Response:
    index = request.GET['index']

    print('Pause with index {}'.format(index))

    await asyncio.sleep(random.random())

    print('Un pause with index {}'.format(index))

    return web.Response(text='Response of {} index'.format(index))

app = web.Application()
app.router.add_route('GET', '/test', test_route)
