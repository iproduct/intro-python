
if __name__ == '__main__':
    num_str = input('Input 4 numbers separated by space:').split()
    numbers = { int(x): int(x) ** 2 for x in num_str }
    print(numbers)