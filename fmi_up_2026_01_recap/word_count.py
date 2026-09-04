import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def word_count(fname):
    wc = {}
    with open(fname) as f:
       for line in f:
           words = re.split(r'\W', line)
           for word in words:
               word = word.lower()
               if word in stop_words or len(word) < 3: continue
               wc[word] = wc.get(word, 0) + 1
    return wc

if __name__ == '__main__':
    wcounts = word_count('wiki.txt')
    wclist = list(wcounts.items())
    wclist.sort(key=lambda x: (-x[1], x[0]))
    print(wclist)