import io
import re
from operator import itemgetter


def itemNumber(item):
    return item[1]

def count(file: io.IOBase) -> list[str]:
    wc = dict()
    for line in file:
        pos = line.find("#")
        if pos >= 0:
            line = line[:pos]
        words = re.split("[\s\.\,\:\;\?\!\"\'\{\}\[\]\(\)\+\=-\\\*]+", line)

        for word in words:
            if word:
                wc[word] = wc.get(word, 0) + 1
    return wc

if __name__ == "__main__":
    # print("Enter file name: ")
    file_name1 = "print_source.py"
    # print("Enter another file name: ")
    file_name2 = "print_source2.py"
    f1 = open(file_name1, "rt", encoding="utf-8")
    f2 = open(file_name2, "rt", encoding="utf-8")

    words1 = count(f1)
    words2 = count(f2)

    words1_sorted = sorted(words1.items(), key=itemgetter(1), reverse=True)
    words2_sorted = sorted(words2.items(), key=itemgetter(1), reverse=True)
    print(words1_sorted)
    print(words2_sorted)
    all_words = set(words1)
    all_words.update(words2)
    # print(all_words)
    results = [(w, words1.get(w, 0), words2.get(w, 0)) for w in all_words]
    # print(results)
    metric = 0
    for r in results:
        metric += abs(r[1] - r[2])
    print(metric / len(results))
