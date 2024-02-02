def fact(n):
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


text = """Hello
from
Python"""

if __name__ == '__main__':
    n = 20
    print(f'{n}! = {fact(n)}')
    print(text)
