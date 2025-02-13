import sys


def sequence(start=0, end=100, step=1):
    nxt = start - step
    def next():
        nonlocal nxt
        nxt += step
        if nxt >= end:
            return None
        return nxt
    return next

def seq_gen(start=0, end = 100, step=1):
    nxt = start
    while nxt < end:
        yield nxt
        nxt += step

if __name__ == '__main__':
    seq1 = sequence(1, 20, 2)
    while True:
        val = seq1()
        if val is None:
            break
        print(val)

    for val in seq_gen(1,20,2):
        print(val)
