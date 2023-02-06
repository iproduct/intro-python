import sys
# sys.set_int_max_str_digits(0)
def fact_iter(n):
    r = 1
    while n > 1:
        r *= n
        n -= 1
    return r

if __name__ == '__main__':
    n = int(input('N='))
    print(f'{n}! = {fact_iter(n)}')