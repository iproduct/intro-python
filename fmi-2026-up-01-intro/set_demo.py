from re import split


def get_unique_words(text):
    """Returns a list of unique words in text."""
    # words_set = set()
    # for word in re.split('\W+', text):
    #     words_set.add(word)
    # words = list(words_set)
    words = list(set(split('\\W+', text)))
    words.sort()
    return words

if __name__ == '__main__':
    with open('wiki_text.txt', 'r') as f:
        text = f.read()
        words = get_unique_words(text)
        print(words)
    squares = {x**2 for x in range(1, 10)}
    print(squares)
    print(type(squares))
    numbers = [18, 42, 33, 4, 152, 62, 78, 88, 98, 10]
    print(numbers)
    print('All even: ', all(x % 2 == 0 for x in numbers))
    print('Exists odd: ', any(x % 2 == 1 for x in numbers))
