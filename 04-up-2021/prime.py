import math

def is_prime(y):
    x = int(math.sqrt(y))
    while x > 1:
        print(x)
        if y % x == 0:
            return False
        x -= 1
    return True

if __name__ == '__main__':
    y = int(input("Input a number:"))
    print(f"Is {y} prime: {is_prime(y)}")