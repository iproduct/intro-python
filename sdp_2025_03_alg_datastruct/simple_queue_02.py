from myqueue import Queue
from queue_ll import QueueLL


def fib_gen(n: int):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    queue: Queue[int] = QueueLL()
    for fib in fib_gen(10):
        queue.enqueue(fib)

    while not queue.is_empty() :
        elem = queue.dequeue()
        print(elem)
    