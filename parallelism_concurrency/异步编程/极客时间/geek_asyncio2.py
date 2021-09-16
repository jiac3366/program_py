import asyncio
import aiohttp
import time


async def download_one(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print('Read {} from {}'.format(resp.content_length, url))


async def download_all(sites):
    tasks = [asyncio.create_task(download_one(site)) for site in sites]
    await asyncio.gather(*tasks)


def mains():
    sites = [
        'https://en.wikipedia.org/wiki/Portal:Arts',
        'https://en.wikipedia.org/wiki/Portal:History',
        'https://en.wikipedia.org/wiki/Portal:Society',
        'https://en.wikipedia.org/wiki/Portal:Biography',
        'https://en.wikipedia.org/wiki/Portal:Mathematics',
        'https://en.wikipedia.org/wiki/Portal:Technology',
        'https://en.wikipedia.org/wiki/Portal:Geography',
        'https://en.wikipedia.org/wiki/Portal:Science',
        'https://en.wikipedia.org/wiki/Computer_science',
        'https://en.wikipedia.org/wiki/Python_(programming_language)',
        'https://en.wikipedia.org/wiki/Java_(programming_language)',
        'https://en.wikipedia.org/wiki/PHP',
        'https://en.wikipedia.org/wiki/Node.js',
        'https://en.wikipedia.org/wiki/The_C_Programming_Language',
        'https://en.wikipedia.org/wiki/Go_(programming_language)'
    ]
    start_time = time.perf_counter()
    asyncio.run(download_all(sites))
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    mains()
# 主函数里的 asyncio.run(coro) 是 Asyncio 的 root call，表示拿到 event loop，运行输入
# 的 coro，直到它结束，最后关闭这个 event loop。事实上，asyncio.run() 是
# Python3.7+ 才引入的，相当于老版本的以下语句：

# loop = asyncio.get_event_loop()
# try:
#     loop.run_until_complete(coro)
# finally:
#     loop.close()
# 这里的asyncio.create_task(coro)，表示对输入的协程 coro 创建一个任务，安排它
# # 的执行，并返回此任务对象。这个函数也是 Python 3.7+ 新增的，如果是之前的版本，你
# # 可以用asyncio.ensure_future(coro)等效替代。可以看到，这里我们对每一个网站
# # 的下载，都创建了一个对应的任务。
