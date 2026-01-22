import strings

def count_vowels(s):
    count = 0
    s = s.lower()
    for c in s:
        if c in 'aeiouy':
            count += 1
    return count

def get_word_points(word):
    vowels = count_vowels(word)
    if vowels % 2 == 0:
        return 2
    else:
        return 1

def get_total_points(line):
    points = 0
    words = line.split()
    for word in words:
        points += get_word_points(word)
    return points


if __name__ == '__main__':
    text = strings.text
    lines = strings.split_lines(text)
    for line in lines:
        line = line.strip()
        if len(line) > 0:
            points = get_total_points(line)
            print(f'{line:70s} -> {points:3d}')