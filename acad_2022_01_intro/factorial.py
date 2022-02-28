
def fact_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    for n in range(1, 1001):
        print(f'{n}! = {fact_iter(n)}')
