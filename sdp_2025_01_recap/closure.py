
def create_counter():
    counter = 0
    def increment():
        nonlocal counter;
        counter += 1
        return counter
    return increment

if __name__ == '__main__':
    counter = create_counter()
    for i in range(10):
        print(counter())