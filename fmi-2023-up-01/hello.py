# This is a sample Python script.
from fibonacci import print_fib


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name, age):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name} - {age} years old!')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_name = input("What's your name?")
    my_age = input("What's your age?")
    print_hi(my_name, my_age)
    print_fib(20)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
