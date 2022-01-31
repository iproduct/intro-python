from nltk.corpus import stopwords
import nltk
import re

nltk.download('stopwords')
en_stops = set(stopwords.words("english"))
# print(en_stops)

if __name__ == '__main__':
    pattern = re.compile("[\W\d]+")
    word_counts = dict()
    with open('wikipedia.txt') as f:
        for i, line in enumerate(f.readlines()):
            str = line.strip()
            if len(str) < 3:
                continue
            words_list = re.split(pattern, str)
            # print(f"{i:03d}: [{len(str)}] {str[:80]}")
            for word in words_list:
                if len(word) < 3 or word in en_stops:
                    continue
                word_counts[word] = word_counts.get(word, 0) + 1

        print(word_counts)
        # words_count_list = list(word_counts.items())
        # words_count_list.sort(key=lambda item: item[1], reverse=True)
        words_count_list = sorted(word_counts.items(), key=lambda item: (-item[1], item[0].lower()))
        for item in words_count_list[:20]:
            print(f"{item[0]:20s} -> {item[1]:3d}")
