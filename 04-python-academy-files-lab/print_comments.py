import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = __file__
    print(f"Opening: {filename}")
    with open(filename, encoding="utf-8") as f:
        for i, line in enumerate(f):
            pos = line.find("#")
            if pos >= 0:
                print(f"{i:3d}: {line[pos + 1: ].strip()}")
