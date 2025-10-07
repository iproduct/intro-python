
if __name__ == '__main__':
    n = int(input("N = "))
    keys = list([0]*n)
    values = list([0]*n)
    for i in range(n):
        keys[i] = input(f'key[{i}] = ')
    for i in range(n):
        values[i] = input(f'value[{i}] = ')
    dictionary = dict()
    for i in range(n):
        dictionary[keys[i]] = values[i]
    print(dictionary)
