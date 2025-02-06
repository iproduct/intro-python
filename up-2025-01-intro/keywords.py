from collections.abc import Iterable
import re

import nltk
from nltk.corpus import stopwords

from os import listdir
from os.path import isfile, join

# nltk.download('stopwords')
stops = set(stopwords.words('english'))

def get_count(word_count: tuple[str, int]) -> int:
    return word_count[1]

def get_keywords(lines: Iterable[str], count = 100) -> list[tuple[str, int]]:
    word_counts = {}
    for line in lines:
        words = re.split('[^a-zA-Z_]+', line)
        for word in words:
            word = word.lower()
            if len(word) < 2 or word in stops:
                continue
            word_counts[word] = word_counts.get(word, 0) + 1
    keywords = list(word_counts.items())
    keywords.sort(key = get_count, reverse = True)
    return keywords[:count]

def index_dir(dirname: str, count = 100) -> dict[str, list[tuple[str, int]]]:
    file_keywords = {}
    files = [join(dirname, f) for f in listdir(dirname) if isfile(join(dirname, f))]
    for filename in files:
        with open(filename, 'rt') as f:
            keywords = get_keywords(f, count)
            file_keywords[filename] = keywords
    return file_keywords

def write_keywords(file_keywords: dict[str, list[tuple[str, int]]], dbfilename: str) -> None:
    with open(dbfilename, 'wt') as db:
        for filename, keywords in file_keywords.items():
            kw_str_list = [f'{keyword[0]}:{keyword[1]}' for keyword in keywords]
            db.write(f'{filename}, {','.join(kw_str_list)}\n')

if __name__ == '__main__':
    file_keywords = index_dir('articles',20)
    write_keywords(file_keywords,'keywords.db')
    for filename, keywords in file_keywords.items():
        print(f'{filename}:')
        for keyword in keywords:
            print(f'       {keyword[0]:30s} -> {keyword[1]:>4d}')