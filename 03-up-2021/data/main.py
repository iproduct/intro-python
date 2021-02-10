import re

def extract_count(item):
    return item[1] # the word count

def remove_comment(line):
    ch = "\""
    start = line.find(ch)
    if start < 0:
        start_comment = line.find("#")
    else:
        start_comment = line.find("#", 0, start)
    if start_comment >= 0:
        line = line[:start_comment]
        return line
    while start >= 0:
        end = line.find(ch, start)
        if end < 0:
            break
        start = line.find(ch, end + 1)
        start_comment = line.find("#", end + 1, start)
        if start_comment > end:
            line = line[:start_comment+1]
            break
    return line

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
        line = line.strip()
        if line == "":
            continue

        words = re.split("[\s.,!\?\-\+\[\](){}:;\"\']+", line)
        # print(words)
        for word in words:
            word_lower_case = word.lower()
            if word_lower_case == "":
                continue
            if word_lower_case in word_counts:
                word_counts[word_lower_case] += 1
            else:
                word_counts[word_lower_case] = 1
    file.close()  # flushes data to disk
    return word_counts

if __name__ == '__main__':
    # 1. input two filenames
    file1 = input("Input the filename 1:")
    file2 = input("Input the filename 2:")
    # 2. Process files
    counts1 = parse_file("data/" + file1)
    counts2 = parse_file("data/" + file2)
    # counts1 = parse_file("data/example01.py")
    # print(counts1)
    # counts2 = parse_file("data/example02.py")
    # print(counts2)

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