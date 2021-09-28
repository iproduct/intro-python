from queue import LifoQueue

if __name__ == '__main__':
   stack = LifoQueue(100)
   stack.put("One")
   stack.put("Two")
   stack.put("Three")
   stack.put("Four")
   stack.put("Five")

   # LIFO order
   while not stack.empty():
       print(stack.get())