if __name__ == '__main__':
    with open("example.txt", "wt") as f:
        f.write("Hello World\n")
        f.write("From Python\n")
        f.write("Script\n")
    with open("example.txt", "rt") as f:
        print(f.readline())
        pos1 = f.tell()
        print(pos1)
        print(f.readline())
        print(f.tell())
        print(f.seek(pos1))
        print(f.readline())
        print(f.readline())
        eof = f.readline()
        print(f"'{eof}', len:{len(eof)}")
    with open("example.txt", "rt") as f:
        for number, line in enumerate(f):
            print(number,':', line[:-1])
    with open("example.txt", "rt") as f:
        lines = f.readlines()
        for line in lines:
            print(line[:-1])

