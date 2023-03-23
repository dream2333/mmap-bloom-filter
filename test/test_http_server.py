# import aiohttp
# import zerorpc
from tools import caculate_time
import asyncio

def test_run_http_client():

    async def fetch(session):
        html = await session.get('http://127.0.0.1:8000/')

    async def main():
        async with aiohttp.ClientSession() as session:
            await asyncio.wait([asyncio.create_task(fetch(session)) for i in range(10000)])
    asyncio.run(main())