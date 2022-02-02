

def fact_iter(n):
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result


def fact_rec(n):
    # recursion bottom
    if n <= 1:
        return 1
    # recursion step
    return n * fact_rec(n - 1)


if __name__ == '__main__':
    n = int(input("Input N:"))
    print(f"Iterative {n}! = ", fact_iter(n))
    print(f"\nRecursive {n}! = ", fact_rec(n))
