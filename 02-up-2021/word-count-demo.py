import re

if __name__ == '__main__':
    file = open("wikipedia.txt", "rt")
    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue
        words = re.split("[\s.,!\?\-\+\[\](){}]+", line)
        print(words)
    file.close()  # flushes data to disk