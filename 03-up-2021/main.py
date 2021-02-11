import re

def extract_count(item):
    return item[1] # the word count

def remove_comment(line):
    parts = re.split(r"\".*\"|'.*'|\"\"\".+\"\"\"", line)
    line = "".join(parts)
    start_comment = line.find("#")
    if start_comment >= 0:
        return line[:start_comment]
    return line
    # end = 0
    # match = re.search("['\"]|\"\"\"", line)
    # while match and end >= 0:
    #     start = match.start() + end
    #     str_chars = line[start:match.end() + end]
    #     start_comment = line.find("#", end, start)
    #     if start_comment >= 0:
    #         return line[:start_comment]
    #     end = line.find(str_chars, start + 1)
    #     match = re.search("['\"]|\"\"\"", line[end+1:])
    # if end >= 0:
    #     start_comment = line.find("#", end)
    #     if start_comment >= 0:
    #         return line[:start_comment]
    # return line

def parse_file(filename):
    word_counts = {}

    # 2. read file line by line
    file = open(filename, "rt", encoding="utf8")
    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue

        # 3. remove comments
        line = remove_comment(line)
        print(line)
        # line = re.sub("#.*", "", line)
        # index = line.find("#")
        # if index >= 0:
        #     line = line[:index]
        line = line.strip()
        if line == "":
            continue

        words = re.split("[\s.,!\?\-\+\[\](){}:;\"\']+", line)
        # print(words)
        for word in words:
            word_lower_case = word.lower()
            if word_lower_case == "":
                continue
            word_counts[word_lower_case] = word_counts.get(word_lower_case, 0) + 1
            # if word_lower_case in word_counts:
            #     word_counts[word_lower_case] += 1
            # else:
            #     word_counts[word_lower_case] = 1
    file.close()  # flushes data to disk
    return word_counts

if __name__ == '__main__':
    # 1. input two filenames
    # file1 = input("Input the filename 1:")
    # file2 = input("Input the filename 2:")
    # 2. Process files
    # counts1 = parse_file("data/" + file1)
    # counts2 = parse_file("data/" + file2)
    counts1 = parse_file("data/example04.py")
    print(counts1)
    counts2 = parse_file("data/example01.py")
    print(counts2)

    #5. sort and print words
    items1 = list(counts1.items())
    items1.sort(key=extract_count, reverse=True)
    for item in items1[:20]:
        print(f"{item[0]:15} -> {item[1]:6}")
    print()

    items2 = list(counts2.items())
    items2.sort(key=extract_count, reverse=True)
    for item in items2[:20]:
        print(f"{item[0]:15} -> {item[1]:6}")

    #6. triples with counts1 counts2
    triples = []
    for k in counts1.keys():
        if k in counts2:
            triples.append((k, counts1[k], counts2[k]))
        else:
            triples.append((k, counts1[k], 0))

    for k in counts2.keys():
        if k not in counts1:
            triples.append((k, 0, counts2[k]))
    print()
    print(triples)

    #7. calculate difference
    sum = 0
    for word, count1, count2 in triples:
        sum += abs(count1 - count2)
    print(f'Calculated difference: {sum / len(triples)}')