from functools import reduce

if __name__ == '__main__':
    product = reduce((lambda x, y: x + str(y)), [n for n in range(1, 10)], "")
    print(product)
