import re

def strip_comments(lines: list[str]) -> list[str]:
    """
    returns lines with stripped comments (starting with #) and empty lines
    :param lines: input lines
    :return: non-empty lines without comments
    """
    global results
    results = []
    for line in lines:
        index = line.find('#')
        if index >= 0:
            modified = line[0:index]
        else:
            modified = line
        modified = modified.strip()
        if len(modified) > 0:
            results.append(modified)
    return results


def count_words(lines: list[str], word_counts: dict[str, int]):
    for line in lines:
        words = re.split('\W+', line)
        for word in words:
            word = word.strip()
            if len(word) > 1:
                word_counts[word] = word_counts.get(word, 0) + 1

def get_count(word: tuple[str, int]) -> int:
    return (word[1], word[0])

def sort_words(word_counts: dict[str, int]) -> list[tuple[str, int]]:
    wc_list = list(word_counts.items())
    wc_list.sort(key=get_count, reverse=True)
    return wc_list


if __name__ == '__main__':
    # 1
    file1 = input('File name 1:')
    file2 = input('File name 2:')

    #2
    with open(file1, 'rt', encoding="utf-8") as f1:
        lines1 = f1.readlines()
    with open(file2, 'rt', encoding="utf-8") as f2:
        lines2 = f2.readlines()

    #3
    no_comments1 = strip_comments(lines1)
    no_comments2 = strip_comments(lines2)

    #4
    wc1 = dict()
    count_words(no_comments1, wc1)
    wc2 = dict()
    count_words(no_comments2, wc2)

    #5
    wc_sorted1 = sort_words(wc1)
    wc_sorted2 = sort_words(wc2)
    print(wc_sorted1)
    print(wc_sorted2)