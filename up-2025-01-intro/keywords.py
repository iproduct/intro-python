from collections.abc import Iterable

def get_keywords(lines: Iterable[str], count = 100) -> list[tuple[str, int]]:
    for line in lines:
        print(line)
    return []

if __name__ == '__main__':
    with open('article.txt', 'rt') as f:
        # lines = f.readlines()
        keywords = get_keywords(f,20)
    for keyword in keywords:
        print(f'{keyword[0]:30s} -> {keyword[1]:>4d}')