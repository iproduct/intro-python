
def is_palindrome(word):
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome2(word):
    reversed_word = word[::-1]
    return reversed_word == word


if __name__ == '__main__':
    words = ["Able was I ere I saw Elba", "une Slave valse nue", "Madam Im Adam"]
    for word in words:
        word = word.lower().replace(' ','')
        print(f"{word:15s} -> {is_palindrome2(word)}")
