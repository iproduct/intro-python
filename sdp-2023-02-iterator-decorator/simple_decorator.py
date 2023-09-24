def absolute_value(f):
    print('Decorator start')

    def wrapper(x):
        result = abs(f(x))
        print('Decorator end')
        return result

    return wrapper


@absolute_value
def my_func(x):
    return x * 2


if __name__ == '__main__':
    print(my_func(-10))
