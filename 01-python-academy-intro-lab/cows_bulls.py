import random

num_digits = 4
num_guesses = 6

def init():
    digits = list(range(0, 10))
    random.shuffle(digits)
    if digits[0] == 0:
        digits[0] = digits[9]
    return digits[:num_digits]

if __name__ == "__main__":
    print(init())