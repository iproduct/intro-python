
def hello_python(name):
    """
    simple function demo
    using name as argument
    """
    print(f'Hello, {name}!')


def conditional_print(number):  # conditional print demo
    if number > 2:
        print(f"{number} is greater than two!")
    elif number == 2:
        print(f"{number} is equal to two!")
    else:
        print(f"{number} is less than two!")

if __name__ == '__main__':
    hello_python('Python Programmer')
    conditional_print(5)
    quantity = 3
    itemno = 567
    price = 49.95
    my_order = f"I want {quantity} pieces of item {itemno} for {price} dollars."
    print(my_order)