import random
import re
import time

if __name__ == '__main__':
    d = {frozenset({1,}): {'a'}, frozenset({2}): {'b'}}
    print(d)

    # random demo
    random.seed(time.time_ns())
    print(random.random())
    print(re.split("", "I love Python."))
    for k, v in d.items():
        print(k, ' -> ', v)
