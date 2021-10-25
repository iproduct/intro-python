"""factorial done recursively and iteratively"""

def fact1(n):
    ans = 1
    for i in range(2, n + 1):
        ans = ans * i
    return ans


def fact2(n):
    if n < 1:
        return 1
    else:
        return n * fact2(n - 1)

if __name__ == '__main__':
    print(fact1(100))
    print(fact2(100))

