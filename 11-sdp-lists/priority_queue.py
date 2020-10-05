from queue import PriorityQueue

q = PriorityQueue()
q.put((3, 'sleep'))
q.put((2, 'code'))
q.put((1, 'eat'))

while not q.empty():
    next_item = q.get()
    print(next_item)
# Резултат:
# (1, 'eat')
# (2, 'code')
# (3, 'sleep')