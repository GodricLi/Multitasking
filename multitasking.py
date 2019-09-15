import asyncio
import requests

"""
这里我们使用一个 for 循环创建了五个 task，
组成了一个列表，然后把这个列表首先传递给了 asyncio 的 wait() 方法，
然后再将其注册到时间循环中，就可以发起五个任务,任务依次执行
"""


async def request():
    url = "https://www.baidu.com"
    status = requests.get(url)
    return status


tasks = [asyncio.ensure_future(request()) for _ in range(5)]
print('Task:', tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
for task in tasks:
    print('Task result:', task.result())
