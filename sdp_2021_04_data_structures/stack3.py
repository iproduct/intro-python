from collections import deque

if __name__ == '__main__':
   queue = deque(['Before first', 'Before second'])
   queue.appendleft("One")
   queue.appendleft("Two")
   queue.appendleft("Three")
   queue.appendleft("Four")
   queue.appendleft("Five")

   # FIFO order
   while len(queue) > 0:
       print(queue.popleft())