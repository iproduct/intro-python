import re

# import nltk
# from nltk.corpus import stopwords

# nltk.download('stopwords')
# en_stops = set(stopwords.words('english'))
#
# print(en_stops)

stop_words = {'when', "didn't", 'wasn', 'y', 'few', 'below', 'into', 'there', 'his', 'these', 'about', 'if', 'again',
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


def index_text(text: str, num_keywords: int = 20) -> list[tuple[str, int]]:
    """
    Index a text by returning top num_keywords keywords with their count as list of tuples
    :param text: input text
    :param num_keywords: number of keywords to be returned
    :return: the extracted top num_keywords keywords
    """
    word_counts = dict()
    lines = text.split("\n")
    for i, line in enumerate(lines):
        line_text = line.strip()
        if len(line_text) == 0:
            continue
        # print(i + 1, ":", line)
        words = re.split(r"[\s.,?!\(\)\{\}\[\];\-_\'\"]", line_text)
        # print(words)
        for word in words:
            if len(word) < 3 or word in stop_words:
                continue
            word_counts[word] = word_counts.get(word, 0) + 1
    # wc_list = list(word_counts.items())
    # wc_list.sort(key=count_key, reverse=True)
    tags = sorted(word_counts.items(), key=count_key, reverse=True)
    return tags[:num_keywords]


def count_key(word_count_tuple):
    return word_count_tuple[1]


if __name__ == '__main__':
    with open("documents/wikipedia.txt", encoding='utf-8') as f:
        print(index_text(f.read(), 30))
