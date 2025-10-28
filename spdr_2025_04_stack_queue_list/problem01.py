from random import randint

if __name__ == "__main__":
    queue1 = list()
    stack_odd = list()
    stack_even = list()
    for i in range(20):
        queue1.insert(0, randint(0, 100))

    while len(queue1) > 0:
        number = queue1.pop()
        print(number, end=' ')
        stack_even.append(number) if number % 2 == 0 else stack_odd.append(number)

    print("\nOdd strack:")
    while len(stack_odd) > 0:
        number = stack_odd.pop()
        print(number, end=' ')

    print("\nEven strack:")
    while len(stack_even) > 0:
        number = stack_even.pop()
        print(number, end=' ')
