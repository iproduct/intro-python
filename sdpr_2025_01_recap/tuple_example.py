

if __name__ == '__main__':
    data = input('Input numbers separated by a comma: ')
    number_strings = data.split(',')
    numbers = [ int(num_str.strip()) for num_str in number_strings ]
    print(numbers)
    tp1 = tuple(numbers)
    tp2 = tuple(reversed(tp1))
    print(tp1)
    print(tp2)
    print(tp1 + tp2)