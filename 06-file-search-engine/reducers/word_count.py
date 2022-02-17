import re

# nltk.download('stopwords')
# en_stops = set(stopwords.words("english"))
# print(en_stops)
from typing import Iterable

SPLIT_PATTERN = re.compile("[\W\d]+")

en_stops = {'when', "didn't", 'wasn', 'y', 'few', 'below', 'into', 'there', 'his', 'these', 'about', 'if', 'again',
            'too', 'were', 'then', 'doing', 'haven', 'such', 'this', 'me', 'the', 'further', 'whom', 'having',
            'mightn', 'both', 'him', 'she', 'don', 'yourselves', 'all', 'do', "it's", 'i', 'what', 'needn', 'had',
            'during', 'weren', "wasn't", 'up', 'will', 'just', 'isn', 'theirs', 'own', 'll', 'hadn', "aren't",
            'while', "hasn't", 'themselves', 're', 'in', "she's", "wouldn't", 'he', "couldn't", 'their', 'more',
            "that'll", 'ain', 't', 'a', 'was', 'but', 'couldn', 'only', 'been', 'so', 'until', 'have', 'from',
            'those', 'or', 'our', 'ourselves', 'as', 'doesn', 'over', 'how', "you'd", 'where', 'itself', 'against',
            'very', "you'll", 'who', "needn't", 'by', 'no', 'each', 'its', 'at', 'we', 'any', 'ours', "mightn't",
            'through', 'does', 'here', 'didn', 'between', 'some', 'which', 'other', 'did', "don't", 'hasn', 'won',
            'not', 'should', "haven't", 'on', 'now', 'with', 'you', 'them', 'himself', 'under', "you've", 'yours',
            'they', 'shouldn', "doesn't", 'of', 'can', 'be', 'above', "weren't", 'wouldn', 'for', 's', 'and',
            "hadn't", 'herself', 'nor', "should've", 'am', 'once', 've', 'an', 'hers', 'myself', 'to', 'her', 'is',
            "shan't", 'are', 'same', 'being', 'your', 'than', 'it', 'aren', 'shan', 'd', 'm', "isn't", 'down',
            "shouldn't", "you're", 'why', 'o', 'yourself', 'has', 'my', 'ma', 'out', 'that', "mustn't", 'because',
            'after', 'before', 'most', 'off', 'mustn', "won't"}


def word_count_reducer(content_lines: Iterable[str], *, max_keywords=100) -> list[tuple[str, int]]:
    """
    Reduces content_lines to list of (word, count) tuples
    :param content_lines: iterable of string lines
    :return: list of (word, count) tuples
    """
    word_counts = dict()
    for line in content_lines:
        # print(line)
        str = line.strip()
        if len(str) < 3:
            continue
        words_list = re.split(SPLIT_PATTERN, str)
        # print(f"{i:03d}: [{len(str)}] {str[:80]}")
        for word in words_list:
            word = word.lower()
            if len(word) < 3 or word in en_stops:
                continue
            word_counts[word] = word_counts.get(word, 0) + 1

    # print(word_counts)
    words_count_list = sorted(word_counts.items(), key=lambda item: (-item[1], item[0].lower()))
    return words_count_list[:max_keywords]
