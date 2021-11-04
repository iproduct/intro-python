

if __name__ == '__main__':
    [print(line, end="") for line in open("wikipedia.txt", "rt") if len(line.strip()) > 0]
    