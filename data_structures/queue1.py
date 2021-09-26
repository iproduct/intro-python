if __name__ == '__main__':
   queue = list()
   queue.insert(0, "One")
   queue.insert(0, "Two")
   queue.insert(0, "Three")
   queue.insert(0, "Four")
   queue.insert(0, "Five")

   # FIFO order
   while len(queue) > 0:
       print(queue.pop())