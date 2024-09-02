def fact_iter(number):
    result = 1
    for i in range(2, number+1):
        result *= i
    return result

if __name__=="__main__":
    print(fact_iter(1000))