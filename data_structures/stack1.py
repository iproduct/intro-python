if __name__ == '__main__':
   stack = list()
   stack.append("One")
   stack.append("Two")
   stack.append("Three")
   stack.append("Four")
   stack.append("Five")

   # LIFO order
   while len(stack) > 0:
       print(stack.pop())