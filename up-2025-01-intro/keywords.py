from collections.abc import Iterable
import re

def get_count(word_count: tuple[str, int]) -> int:
    return word_count[1]

def get_keywords(lines: Iterable[str], count = 100) -> list[tuple[str, int]]:
    word_counts = {}
    for line in lines:
        words = re.split('[^a-zA-Z_]+', line)
        for word in words:
            if len(word) < 2:
                continue
            word = word.lower()
            word_counts[word] = word_counts.get(word, 0) + 1
    keywords = list(word_counts.items())
    keywords.sort(key = get_count, reverse = True)
    return keywords[:count]

if __name__ == '__main__':
    with open('article.txt', 'rt') as f:
        # lines = f.readlines()
        keywords = get_keywords(f,20)
    for keyword in keywords:
        print(f'{keyword[0]:30s} -> {keyword[1]:>4d}')