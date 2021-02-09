if __name__ == '__main__':
    # open own source code
    file = open("print-own-source.py", "rt")
    i = 1
    # interate over lines in file
    for line in file:
        line = line.strip()
        print(f"{i}: {line}")
        i += 1

    file.close()  # flushes data to disk