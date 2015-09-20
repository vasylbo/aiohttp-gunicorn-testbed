import asyncio
import aiohttp
from gunicorn_conf import bind as host


async def send_message(url, index):
    response = await aiohttp.get(url=url, params={'index': index})
    print(response)
    await response.release()  # otherwise will throw Unclosed response error

loop = asyncio.get_event_loop()


url = 'http://' + host + '/test'
tasks = [asyncio.ensure_future(send_message(url, i)) for i in range(0, 100)]
loop.run_until_complete(asyncio.wait(tasks))


