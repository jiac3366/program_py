import asyncio
import httpx


async def request():
    async with httpx.AsyncClient() as client:
        # client是一个协程对象 默认不运行 只有在前面加上await调用才运行
        response = await client.get('http://127.0.0.1:8000/sleep/3')
        result = response.json()
        print(result)


asyncio.run(request())