
if __name__ == '__main__':
    file = open('line_numbers.py', mode='rt', encoding='utf-8')
    for i, line in enumerate(file, 1):
        print(i, ":", line.strip())
    file.close()