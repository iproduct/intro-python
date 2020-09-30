
class Stack:
    def __init__(self, values = []):
        self.__stack = values

    def push(self, value):
        self.__stack.append(value)

    def pop(self):
        return self.__stack.pop()

    def peek(self):
        return self.__stack[-1]

    def __len__(self):
        return len(self.__stack)

if __name__== '__main__':
    stack = Stack()
    stack.push('a')
    stack.push('b')
    stack.push('c')
    stack.push('d')
    stack.push('e')
    stack.push('f')

    print (f'Size: {len(stack)}')
    print (f'Top: {stack.peek()}')

    while len(stack) > 0:
        print(stack.pop())
