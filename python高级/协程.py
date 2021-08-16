import asyncio



# async 是修饰词 修饰这是1个异步函数 调用不会执行，而会返回一个协程对象
# await是用来调用协程 效果和正常执行一样
# await使用场景: 1 调用协程的有关对象、函数 2 I/O或网络等待的代码前
async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    # 我们要等所有任务都结束
    for task in tasks:
        await task
    # tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    #     # await asyncio.gather(*tasks)


# 或者 *tasks 解包列表，将列表变成了函数的参数；与之对应的是， ** dict 将字典变成了函数的参数。
# async def main(urls):
#   tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
#   await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))



