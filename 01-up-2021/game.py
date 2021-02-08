import random

number_digits = 5
digits = list(range(0, 10))

def init():
    global digits
    random.shuffle(digits)
    if(digits[0] == 0):
        digits[0] = digits[9]
    digits = digits[:number_digits]

def get_bulls_cows(number):
    global digits
    num_str = str(number)
    characters = list(num_str)
    ans_digits = []
    for ch in characters:
        ans_digits.append(int(ch))
    print(ans_digits)
    bulls = 0
    cows = 0
    for i in range(number_digits):
        if ans_digits[i] == digits[i]:
            bulls += 1
        elif ans_digits[i] in digits:
            cows += 1
    return bulls, cows


if __name__ == '__main__':
    init()
    finished = False
    print(digits)
    while not finished:
        answer = input("You number:")
        if len(answer) != number_digits:
            print(f"Should be {number_digits} digits")
            continue
        ans_number = int(answer)
        bulls, cows = get_bulls_cows(ans_number)
        print(f"Bulls {bulls}, Cows: {cows}")
        if bulls == number_digits:
            print("Congratulations you win!")
            finished = True

    print("Good bye!")