import re
from nltk.corpus import stopwords


nltk_words = list(stopwords.words('english'))
def word_statistics(file_name: str) -> dict[str, int]:
    """
    Returns words statistics in form of word -> count of occurrences
    :param file_name: the name of the text file to process
    :return: dictionary of words to word counts numbers
    """
    words = {}
    with open(file_name, 'rt') as f:
        for line in f:
            line_words = [word for word in re.split(r'\W', line) if len(word) > 2]
            if len(line_words) == 0:
                continue
            for word in line_words:
                word = word.lower()
                if word in nltk_words:
                    continue
                if word in words:
                    words[word] = words[word] + 1
                else:
                    words[word] = 1
    return words


if __name__ == "__main__":
    words_dict = word_statistics('wiki_text.txt')
    words_list = list(words_dict.items())
    words_list.sort(key=lambda item: item[1], reverse=True)
    print(words_list[:10])
