from queue import Queue

if __name__ == '__main__':
   queue = Queue(100)
   queue.put("One")
   queue.put("Two")
   queue.put("Three")
   queue.put("Four")
   queue.put("Five")

   # FIFO order
   while not queue.empty():
       print(queue.get())