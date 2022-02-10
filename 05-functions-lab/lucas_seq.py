cache = {}

def lucas(p, q, n):
    print(f"Calling Lucas:", p, q, n)
    if n in cache:
        print(f"Returning:", n, cache[n])
        return cache[n]

    if n == 0:
        return 0

    if n == 1:
        return 1

    result = p * lucas(p, q, n - 1) - q * lucas(p, q, n - 2)
    cache[n] = result
    return result


if __name__ == '__main__':
    p = int(input())
    q = int(input())
    n = int(input())
    # for i in range(3,n+1):
    #     cache = {}
    print(lucas(p, q, n))