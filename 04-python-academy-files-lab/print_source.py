

if __name__ == "__main__":
    for i, line in enumerate(open("print_source.py", "rt")):
        print(f"{i:3d}: {line}", end="")