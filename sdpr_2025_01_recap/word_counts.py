if __name__ == '__main__':
    word_counts = {}
    while True:
        word = input('Enter a word: ')
        if word == '':
            break
        word_counts[word] = word_counts.get(word, 0) + 1
    print(word_counts)