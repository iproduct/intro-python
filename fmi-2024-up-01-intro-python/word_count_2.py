import re
import nltk
from nltk.corpus import stopwords

if __name__ == '__main__':
    nltk.download('stopwords')
    # print(stopwords.words('english'))
    stopwords_set = set(stopwords.words())

    filename = input('Input file name [ENTER for sample.txt]:').strip()
    if filename == '':
        filename = 'sample.txt'
    f = open(filename, 'rt', encoding='utf-8')
    word_counts = dict()
    for line in f:
        words = re.split(r'[^a-zA-Z_\-]+', line.lower())
        for word in words:
            if word in stopwords_set:
                continue
            if word == '':
                break
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    f.close()

    wc_list = sorted(word_counts.items(), key=lambda wc: wc[1], reverse=True)
    print(wc_list[:10])