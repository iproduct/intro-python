

def fact_iter(n):
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

if __name__ == '__main__':
    n = int(input("Input N:"))
    print(f"{n}! = ", fact_iter(n))
