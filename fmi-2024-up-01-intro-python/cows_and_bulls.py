import random

MAX_ATTEMPTS = 8
def generate_number():
    l = [n for n in range(0, 10)]
    while l[0] == 0:
        random.shuffle(l)
    return l[:4]


def find_cows_and_bulls(number: list[int], guess: list[int]) -> (int, int):
    """
    function calcuates number of cows and bulls as a tuple
    :param number: the secret number
    :param guess: the player's guess number
    :return: tuple (cows, bulls)
    """
    bulls = cows = 0
    for i in range(4):
        if guess[i] in number: # cow
            if guess[i] == number[i]: #bull
                bulls += 1
            else:
                cows += 1
    return cows, bulls

if __name__ == "__main__":
    number = generate_number()
    print(number)
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        try:
            guess_num = int(input("Enter your guess:"))
        except ValueError:
            print('Invalid number - try again.')
            continue
        guess = [int(digit) for digit in list(str(guess_num))]
        if len(set(guess)) != 4:  # there are repeated digit in the number
            print('Invalid attempt - try again.')
            continue
        print(guess)
        cows, bulls = find_cows_and_bulls(number, guess)
        if bulls == 4:
            print("Congratulations! You win!!!")
            break
        print(f'Cows: {cows}, Bulls:{bulls}')
        attempts += 1
    else:
        print("Sorry you have exceeded your max attempts.")

