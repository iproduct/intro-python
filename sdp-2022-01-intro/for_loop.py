def char_count_count(char_count):
    return char_count[1]


if __name__ == '__main__':
    for i in range(10, 101, 10):
        print(i)

    char_counts = {}
    for index, fruit in enumerate(['Orange', 'Apple', 'Pineapple', 'Banana', 'Apricot']):
        print(index, '->', fruit)
        for ch in fruit:
            ch = ch.lower()
            char_counts[ch] = char_counts.get(ch, 0) + 1
            print(ch, end=', ')
        print()

    # for key in char_counts:
    #     print(key, '->', char_counts[key])

    char_counts_list = list(char_counts.items())
    char_counts_list.sort(key=lambda char_count: char_count[1], reverse=True)
    print(char_counts_list)
