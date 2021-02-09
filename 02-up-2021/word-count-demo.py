

if __name__ == '__main__':
    file = open("wikipedia.txt", "rt")
    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue
        words = line.split(" ")
        print(words)
    file.close()  # flushes data to disk