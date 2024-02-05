if __name__ == '__main__':
    word_counts = dict()
    while True:
        s = input('Input next word [ENTER to finish]:').strip()
        if s == '':
            break
        if s in word_counts:
            word_counts[s] += 1
        else:
            word_counts[s] = 1

    print(word_counts)