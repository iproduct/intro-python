import asyncio
import time
from asyncio import sleep
from typing import Callable

# async def main():
#     results = await asyncio.gather(async_f(1), async_g(5))
#     print(results)

async def main():
    task1 = asyncio.create_task( async_f(1))
    task1.add_done_callback(lambda res: print(res.result()))
    task2 = asyncio.create_task( async_g(5))
    task2.add_done_callback(lambda res: print(res.result()))
    await asyncio.wait([task1, task2])

async def async_f(x: int):
    await sleep(3)
    return 'f() result'


async def async_g(y: int):
    await sleep(2)
    return "g() result"

if __name__ == '__main__':
    result = asyncio.run(main())
    print(result)