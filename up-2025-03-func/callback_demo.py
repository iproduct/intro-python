import asyncio
import time
from typing import Callable


def callback_f(x: int, callback: Callable[[int],None]):
    time.sleep(3) # simulate computation
    callback(x + 1)

if __name__ == '__main__':
    result = callback_f(5, print)
    print(result)