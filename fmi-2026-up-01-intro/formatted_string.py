import strings

def print_formatted(lines, num_words):
    for line in lines:
        words = strings.split_words(line)
        if len(words) >= num_words:
            row = "|"
            for i in range(num_words):
               row += f" {words[i]:^10.10s} |"
            print(row)


if __name__ == "__main__":
    text = strings.text
    lines = strings.split_lines(text)
    print_formatted(lines, 3)