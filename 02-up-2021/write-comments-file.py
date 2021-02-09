
# function removes strings from text line
# using provided string_char as delimiter
def remove_string(string_char, line):
    start = line.find(string_char)
    while start >= 0:
        end = line.find(string_char, start + 1)
        if end > start:
            line = line[:start] + line[end + 1:]
        start = line.find(string_char, start + 1)
    return line

if __name__ == '__main__':
    # open own source code
    file = open("write-comments-file.py", "r")
    out = open("comments.txt", "w")
    i = 1
    # interate over lines in file
    for line in file:
        line = line.strip()
        line = remove_string("\"", line)
        line = remove_string("'", line)

        index = line.find("#")
        if index >= 0:
            out.write(f"{i}: {line[index+1:]}\n")
            print(f"{i}: {line[index+1:]}")
            i += 1

    out.close() # auto flush data to disk
    file.close()  # flushes data to disk
