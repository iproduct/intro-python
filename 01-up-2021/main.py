# Press Shift+F10 to execute it or replace it with your code.

def print_hi(name):
    print(f'Hi, {name}!') # python 3.8+

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0: # recursion bootm
        return a
    return gcd(b, a % b) # recursion step

def calculate_pi(n):
    percent = n /100
    acc = 0
    for i in range(n):
        if i % percent == 0:
            print(chr(0x25A9), sep="", end="")
        acc += 4.0 * (1 - (i % 2) * 2) / (2 * i + 1)
    return acc


if __name__ == '__main__':
    # name = input("Enter your name:")
    # print_hi(name)
    # print(gcd(222, 234))
    print("\n", calculate_pi(100000000))

