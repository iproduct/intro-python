"""
Provides utility functions for printing fibonacci numbers
"""

def print_fib(n):
    """
    Prints  first n+1 fibonacci numbers to the console
    :param n: the last fibonacci number to be printed
    """
    a, b, index = 0, 1, 0
    while index <= n:
        print(f'fib({index}) = {a}')
        a, b = b, a + b
        index += 1

def print_fib2(n):
    """
        Prints  first n+1 fibonacci numbers to the console using for-in-range
        :param n: the last fibonacci number to be printed
        """
    a, b = 0, 1
    for index in range(0, n + 1, 1):
        print(f'fib({index}) = {a}')
        a, b = b, a + b

if __name__ == '__main__':
    print_fib2(100)