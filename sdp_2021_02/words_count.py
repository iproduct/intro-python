from os.path import exists
import re
from stop_words import get_stop_words

stop_words = get_stop_words('english')
# print(stop_words)

def count_words(filename: str) -> dict[str, int]:
    """
    reads text file with name filename and counts distinct word frequencies in it
    :param filename: the name of the text file
    :return: dict of words -> word counts, or empty dict if file does not exist
    """
    results = {}
    if not exists(filename):
        return results
    with open(filename, 'rt', encoding='utf-8') as f:
        for line in f:
            l = line.strip()
            if l == '':
                continue
            words = re.split('[\s\.!?,;\[\]():\-=_\'"]+', l)
            for word in words:
                word = word.lower()
                if len(word) > 2 and not word.isnumeric() and not word in stop_words:
                    results[word] = (results[word] + 1) if word in results else 1
    return results

if __name__ == '__main__':
    word_counts = count_words('wiki_text01.txt')
    # sort words by count
    word_counts_sorted = sorted(word_counts.items(), key = lambda item: item[1], reverse = True )
    print(word_counts_sorted[:20])


