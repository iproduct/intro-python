import re
from typing import Iterable
from list_files_in_dir import list_files_in_dir

# import nltk
# from nltk.corpus import stopwords

# nltk.download('stopwords')
# en_stops = set(stopwords.words('english'))
#
# print(en_stops)

PYTHON_DOCS_DIR = r"D:\CoursePython\python_docs\python-3.10.2-docs-html"

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


def index_text(lines: Iterable[str], num_keywords: int = 20, case_sensitive = False) -> list[tuple[str, int]]:
    """
    Index a text by returning top num_keywords keywords with their count as list of tuples
    :param text: input text
    :param num_keywords: number of keywords to be returned
    :param case_sensitive : if the word counting should be case-sensitive
    :return: the extracted top num_keywords keywords
    """
    word_counts = dict()
    for line in lines:
        line_text = line.strip()
        if len(line_text) == 0:
            continue
        words = re.split(r"[\s.,?!\(\)\{\}\[\];\-_\'\"]", line_text)
        for word in words:
            word_lower = word.lower()
            if len(word) < 3 or word_lower in stop_words:
                continue
            if not case_sensitive:
                word = word_lower
            word_counts[word] = word_counts.get(word, 0) + 1
    # wc_list = list(word_counts.items())
    # wc_list.sort(key=count_key, reverse=True)
    tags = sorted(word_counts.items(), key=count_key, reverse=True)
    return tags[:num_keywords]

def remove_tags(markup_lines: Iterable[str]) -> Iterable[str]:
    """
    Filter out markup from document using line Iterables
    :param markup: html or xml markup as Iterable of text lines
    :return: filtered plain text (content only without tags) as Iterable of content lines
    """
    for line in markup_lines:
        content = ""
        start = 0
        end = -1
        while start >= 0:
            start = line.find("<", end  + 1)
            if start < 0:
                content += line[end + 1:]
            else:
                content += line[end + 1:start]
                end = line.find(">", start + 1)
                if end < 0:
                    break
        content = content.strip()
        if len(content) > 0:
            yield content


def count_key(word_count_tuple):
    return word_count_tuple[1]


if __name__ == '__main__':
    search_index = {}
    for dir_entry in list_files_in_dir(PYTHON_DOCS_DIR):
        with open(dir_entry.path, encoding='utf-8') as f:
            text_lines = remove_tags(f)
            # for content in text_lines:
            #     # print(bytes(content, encoding='utf-8'))
            #     print(content)
            search_index[dir_entry.path] = index_text(text_lines, 30)
            print(f"| {dir_entry.path:70.70s} | {str(search_index[dir_entry.path]):50.50s} |")

    # print results
    # for path in search_index:
    #     print(f"| {path:70.70s} | {', '.join(search_index[path]): 50.50s} |")