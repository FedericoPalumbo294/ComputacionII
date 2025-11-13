#!/usr/bin/env python3
import asyncio
import aiohttp
import sys


async def main():
    if len(sys.argv) != 3:
        print("Uso: client.py <server_url> <target_url>")
        print("Ej: client.py http://127.0.0.1:8000 https://example.com")
        return

    server = sys.argv[1]
    target = sys.argv[2]

    async with aiohttp.ClientSession() as session:
        async with session.get(f"{server}/scrape", params={"url": target}) as resp:
            data = await resp.json()
            print(data)


if __name__ == "__main__":
    asyncio.run(main())
