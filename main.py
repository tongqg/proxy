#!/usr/bin/env python
# author tongqg

import aiohttp
import asyncio
import async_timeout
from aiohttp import web

async def fetch(session, url):
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

async def get():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://python.org')
        return html

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

async def handle(request):
    # name = request.match_info.get('name', "Anonymous")
    # text = "Hello, " + name
    # return web.Response(text=text)
    text = await get()
    return web.Response(text=text)


app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/{name}', handle)

web.run_app(app)
