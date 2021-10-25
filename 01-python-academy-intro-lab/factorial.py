
def factorialIter(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorialRec(n):
    if n == 1:
        return 1
    else:
        return n * factorialRec(n - 1)

if __name__ == '__main__':
    print(factorialIter(100))
    print(factorialRec(100))