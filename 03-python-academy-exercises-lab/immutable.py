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
    print("           I love Python.        ".strip(),"|", sep="")
    print("int: {0:10d};  hex: {1:8.3f};  oct: {0:o};  bin: {0:b}".format(42, 3.1412313))