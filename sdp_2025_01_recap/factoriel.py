import sys


def fact(n):
    if n == 0: #recursion bottom
        return 1
    else:
        return n * fact(n-1) #recursion step

if __name__ == '__main__':
    sys.setrecursionlimit(2000)
    sys.set_int_max_str_digits(10000)
    f = fact(1998)
    print(f)