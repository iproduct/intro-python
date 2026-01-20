import sys

def fact_iter(n):
    factorial = 1
    for i in range(1, n+1):
        factorial =  factorial * i
    return factorial

def fact_rec(n):
    if n == 1:                   # recursion bottom
        return 1
    else:
        return n * fact_rec(n-1) # recursion step


if __name__ == '__main__':
    sys.set_int_max_str_digits(100000)
    sys.setrecursionlimit(1500)
    # name = input("Enter your name:")
    # print(type(name))
    # print("Hello " + name + ", from python world.")
    print('Iter:', fact_iter(1000))
    print("Rec:", fact_rec(1000))
    # print(type(fact_rec(1000)))