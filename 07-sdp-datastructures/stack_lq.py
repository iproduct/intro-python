from queue import LifoQueue

if __name__ == '__main__':
    stack = LifoQueue()
    stack.put('one')
    stack.put('two')
    stack.put('three')
    stack.put('four')
    stack.put('five')
    stack.put('six')

    while not stack.empty():
        print(stack.get())