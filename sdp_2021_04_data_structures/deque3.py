from collections import deque

if __name__ == '__main__':
   queue = deque(['Before first', 'Before second'])
   queue.appendleft("One")
   queue.appendleft("Two")
   queue.append("Three")
   queue.append("Four")
   queue.appendleft("Five")

   # FIFO order
   while len(queue) > 0:
       print(queue.popleft())