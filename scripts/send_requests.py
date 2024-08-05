import aiohttp
import asyncio

async def send_request(session, url):
    print("Sending request to", url)
    async with session.get(url) as response:
        return await response.text()

async def main():
    url = "http://localhost:5000/home"
    tasks = []

    async with aiohttp.ClientSession() as session:
        for _ in range(10000):
            task = asyncio.ensure_future(send_request(session, url))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)

# Run the script
asyncio.run(main())