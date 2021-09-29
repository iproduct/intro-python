def outer():
    x = 'John'
    def inner():
        nonlocal x
        x = 'Jane' #nonlocal
    inner()
    return x

if __name__ == '__main__':
    print(outer())