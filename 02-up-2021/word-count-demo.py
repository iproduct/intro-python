import re

stop_words = {'ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 
'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 
'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 
'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 
'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 
'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 
'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 
'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 
'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 
'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than'}

def extract_count(item):
    return item[1] # the word count

if __name__ == '__main__':
    word_counts = {}

    file = open("wikipedia.txt", "rt")
    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue
        words = re.split("[\s.,!\?\-\+\[\](){}]+", line)
        # print(words)
        for word in words:
            word_lower_case = word.lower()
            if word_lower_case in stop_words or len(word_lower_case) < 3:
                continue
            if word_lower_case in word_counts:
                word_counts[word_lower_case] += 1
            else:
                word_counts[word_lower_case] = 1

    word_items = list(word_counts.items())
    word_items.sort(key = extract_count, reverse = True)
    for item in word_items[:10]:
        # print("%-15s -> %6d"%(item[0], item[1]))
        print(f"{item[0]:15} -> {item[1]:6}")

    file.close()  # flushes data to disk