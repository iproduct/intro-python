import re
import nltk

from nltk.corpus import stopwords

nltk.download('stopwords')
stops = set(stopwords.words('english'))

print(stops)

def index_file(file_name: str, max_words: int = 20) -> list[tuple[str, int]]:
    word_counts = {}
    with open(file_name, mode='rt', encoding='utf-8') as f:
        for line in f:
            words = re.split(r'\W+', line)
            for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1
    print(word_counts)

if __name__ == '__main__':
    for word_count in index_file("wikipedia.txt"):
        print(f'{word_count[0]:30s} -> {word_count[0]:4d}')