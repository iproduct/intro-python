
def fib_rec(n: int) -> int:
    if n < 2:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)

if __name__ == '__main__':
    for n in range(0, 21):
        print(fib_rec(n), end= ', ')