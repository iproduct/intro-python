
if __name__ == '__main__':
    with open('print_file_lines.py', 'r', encoding='utf-8') as f:
        for (n, line) in enumerate(f, start=1):
            print(f'{n:>3d}: {line}', end='')