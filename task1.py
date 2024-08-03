"""task1.py"""

import asyncio
import aiohttp
import requests
from time import time

def fetch_url(url):
    p = requests.get(url)
    return p.text

async def fetch_all_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url_async(session, url) for url in urls]
        return await asyncio.gather(*tasks)

async def fetch_url_async(session, url):
    async with session.get(url, ssl=False) as response:
        return await response.text()

if __name__ == "__main__":
    URLS = ['https://jsonplaceholder.typicode.com/todos/1'] * 100

    start_time = time()
    for url in URLS:
        fetch_url(url)
    end_time = time()
    print("Classic way:", end_time - start_time)

    start2_time = time()
    asyncio.run(fetch_all_urls(URLS))
    end2_time = time()
    print("Asyncio way:", end2_time - start2_time)