import re
# import nltk
# from nltk.corpus import stopwords

# nltk.download('stopwords')
# en_stops = set(stopwords.words('english'))
#
# print(en_stops)

stop_words = {'when', "didn't", 'wasn', 'y', 'few', 'below', 'into', 'there', 'his', 'these', 'about', 'if', 'again', 'too', 'were', 'then', 'doing', 'haven', 'such', 'this', 'me', 'the', 'further', 'whom', 'having', 'mightn', 'both', 'him', 'she', 'don', 'yourselves', 'all', 'do', "it's", 'i', 'what', 'needn', 'had', 'during', 'weren', "wasn't", 'up', 'will', 'just', 'isn', 'theirs', 'own', 'll', 'hadn', "aren't", 'while', "hasn't", 'themselves', 're', 'in', "she's", "wouldn't", 'he', "couldn't", 'their', 'more', "that'll", 'ain', 't', 'a', 'was', 'but', 'couldn', 'only', 'been', 'so', 'until', 'have', 'from', 'those', 'or', 'our', 'ourselves', 'as', 'doesn', 'over', 'how', "you'd", 'where', 'itself', 'against', 'very', "you'll", 'who', "needn't", 'by', 'no', 'each', 'its', 'at', 'we', 'any', 'ours', "mightn't", 'through', 'does', 'here', 'didn', 'between', 'some', 'which', 'other', 'did', "don't", 'hasn', 'won', 'not', 'should', "haven't", 'on', 'now', 'with', 'you', 'them', 'himself', 'under', "you've", 'yours', 'they', 'shouldn', "doesn't", 'of', 'can', 'be', 'above', "weren't", 'wouldn', 'for', 's', 'and', "hadn't", 'herself', 'nor', "should've", 'am', 'once', 've', 'an', 'hers', 'myself', 'to', 'her', 'is', "shan't", 'are', 'same', 'being', 'your', 'than', 'it', 'aren', 'shan', 'd', 'm', "isn't", 'down', "shouldn't", "you're", 'why', 'o', 'yourself', 'has', 'my', 'ma', 'out', 'that', "mustn't", 'because', 'after', 'before', 'most', 'off', 'mustn', "won't"}

text = """
Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[30]

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[31][32]

Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.[33] Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a cycle-detecting garbage collection system (in addition to reference counting). Python 3.0 was released in 2008 and was a major revision of the language that is not completely backward-compatible. Python 2 was discontinued with version 2.7.18 in 2020.[34]

Python consistently ranks as one of the most popular programming languages.[35][36][37][38]


Contents
History

The designer of Python, Guido van Rossum, at OSCON 2006
Main article: History of Python
Python was conceived in the late 1980s[39] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC programming language, which was inspired by SETL,[40] capable of exception handling and interfacing with the Amoeba operating system.[10] Its implementation began in December 1989.[41] Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his "permanent vacation" from his responsibilities as Python's "benevolent dictator for life", a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker.[42] In January 2019, active Python core developers elected a five-member "Steering Council" to lead the project.[43][44]

Python 2.0 was released on 16 October 2000, with many major new features, including a cycle-detecting garbage collector (in addition to reference counting) for memory management and support for Unicode.[45]

Python 3.0 was released on 3 December 2008. It was a major revision of the language that is not completely backward-compatible.[46] Many of its major features were backported to Python 2.6.x[47] and 2.7.x version series. Releases of Python 3 include the 2to3 utility, which automates the translation of Python 2 code to Python 3.[48]

Python 2.7's end-of-life date was initially set at 2015 then postponed to 2020 out of concern that a large body of existing code could not easily be forward-ported to Python 3.[49][50] No more security patches or other improvements will be released for it.[51][52] With Python 2's end-of-life, only Python 3.6.x[53] and later are supported.

Python 3.9.2 and 3.8.8 were expedited[54] as all versions of Python (including 2.7[55]) had security issues, leading to possible remote code execution[56] and web cache poisoning.[57]
"""

def count_key(word_count_tuple):
    return word_count_tuple[1]

if __name__ == '__main__':
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
            if len(word) < 3:
                continue
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    wc_list = list(word_counts.items())
    wc_list.sort(key=count_key, reverse=True)
    print(wc_list)