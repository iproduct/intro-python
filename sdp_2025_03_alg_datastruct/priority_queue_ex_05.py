from queue import PriorityQueue

if __name__ == '__main__':
    q = PriorityQueue()
    q.put((2, 'code'))
    q.put((1, 'eat'))
    q.put((3, 'sleep'))
    while not q.empty():
        next_item = q.get()
        print(next_item)
        # Резултат:
        # (1, 'eat')
        # (2, 'code')
        # (3, 'sleep')
        