import strings
import nltk
from nltk.corpus import stopwords
# from nltk.tokenize import
import re

nltk.download('stopwords')
# nltk.download('punkt')

stop_words = set(stopwords.words('english'))

def count_frequencies(text):
    word_frequencies = dict() #  or {}
    for word in re.split(r'\W+', text):
        word = word.lower()
        if len(word) < 2 or word.isdecimal() or word in stop_words:
            continue
        # if word in word_frequencies:
        #     word_frequencies[word] += 1
        # else:
        #     word_frequencies[word] = 1
        word_frequencies[word] = word_frequencies.get(word, 0) + 1
    return word_frequencies

def topn_words_frequencies(word_frequencies, num_words):
    words_counts = []
    for word in word_frequencies:
        words_counts.append((word_frequencies[word], word))
    words_counts.sort(reverse=True)
    return words_counts[:num_words]


if __name__ == '__main__':
    with open('wiki_text.txt', 'r') as myfile:
        text = myfile.read()
    word_frequencies = count_frequencies(text)
    print(topn_words_frequencies(word_frequencies, 10))