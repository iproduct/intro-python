def fib(n):
    """
    Calculate and return n-th fibonacci sequence number
    :param n: element number in fubonacci sequence
    :return: the value of n-th fibonacci number
    """
    a, b = 0, 1
    while n:
        a, b = b, a + b
        n -= 1
    return a

def fib_gen(n):
    """
    Calculate and return n-th fibonacci sequence number
    :param n: element number in fubonacci sequence
    :return: the value of n-th fibonacci number
    """
    a, b = 0, 1
    while n:
        yield a
        a, b = b, a + b
        n -= 1


if __name__ == "__main__":
    for x in fib_gen(20):
        print(x)
    print("End of demo.")