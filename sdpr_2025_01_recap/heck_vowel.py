
def is_vowel(letter):
    vowels = "aeiouAEIOU"
    if letter in vowels:
        return True
    else:
        return False

if __name__ == '__main__':
    while True:
        letter = input('Enter a letter [ENTER for end]: ')
        if letter == '':
            break
        print(f'{letter} is vowel: {is_vowel(letter[0])}')
