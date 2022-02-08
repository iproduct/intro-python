def print_text(filename):
    with open(filename, "rt", encoding="utf-8") as f:
        for i, line in enumerate(f):
            print(i + 1, ":", line.rstrip())

if __name__ == '__main__':
    print_text("print_source.py")
