def strip_comments(lines: list[str]) -> list[str]:
    """
    returns lines with stripped comments (starting with #) and empty lines
    :param lines: input lines
    :return: non-empty lines without comments
    """
    global results
    results = []
    for line in lines:
        index = line.find('#')
        if index >= 0:
            modified = line[0:index]
        else:
            modified = line
        modified = modified.strip()
        if len(modified) > 0:
            results.append(modified)
    return results


if __name__ == '__main__':
    # 1
    file1 = input('File name 1:')
    file2 = input('File name 2:')

    #2
    with open(file1, 'rt', encoding="utf-8") as f1:
        lines1 = f1.readlines()
    with open(file2, 'rt', encoding="utf-8") as f2:
        lines2 = f2.readlines()

    #3
    no_comments1 = strip_comments(lines1)
    no_comments2 = strip_comments(lines2)
    print(no_comments1)
    print(no_comments2)