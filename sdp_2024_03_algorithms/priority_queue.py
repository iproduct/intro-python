from queue import PriorityQueue

if __name__ == '__main__':
    pq = PriorityQueue()
    pq.put((2, 'code'))
    pq.put((1, 'eat'))
    pq.put((3, 'sleep'))

    while not pq.empty():
        print(pq.get())