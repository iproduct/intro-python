from queue import Queue

if __name__ == '__main__':
    queue = Queue()
    queue.put('one')
    queue.put('two')
    queue.put('three')
    queue.put('four')
    queue.put('five')
    queue.put('six')

    while not queue.empty():
        print(queue.get())