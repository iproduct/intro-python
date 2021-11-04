import re
import sys
from operator import itemgetter, attrgetter
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
en_stops = set(stopwords.words('english'))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "wikipedia.txt"
    print(f"Opening: {filename}")
    pattern = re.compile("[\s\.!\?\'\"\[\]\{\},;—\-\d]+")
    word_counts = dict()
    with open(filename, encoding="utf-8") as f:
        for line in f:
            words = re.split(pattern, line)
            for word in words:
                if len(word) > 2 and word not in en_stops:
                    word_counts[word] = word_counts.get(word, 0) + 1
                    # word_counts[word] = (word_counts[word] + 1) if word in word_counts else 1

    # words_count_list = list(word_counts.items())
    # def get_count(tup):
    #     return tup[1]
    # words_count_list.sort(key=get_count, reverse=True)
    # words_sorted = sorted(word_counts, key= word_counts.__getitem__, reverse=True)
    words_sorted = sorted(word_counts.items(), key=itemgetter(1), reverse=True)
    print( words_sorted[:20])
