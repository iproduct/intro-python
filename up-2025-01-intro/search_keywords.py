from keywords import print_file_keywords, get_count


def load_kewords(dbfilename: str) -> dict[str, dict[str, int]]:
    results = {}
    with open(dbfilename) as db:
        for line in db:
            parts = line.split(',')
            filename = parts[0]
            keywords = {}
            for word_count in parts[1:]:
                word, count = word_count.split(':')
                keywords[word] = int(count)
            results[filename] = keywords
    return results

def calc_similarity(keyword_counts: dict[str, int], word: str) -> float:
    total_count = sum(keyword_counts.values())
    if word in keyword_counts:
        return keyword_counts[word] / total_count
    return 0

def search(kw_list: list[str], db: dict[str, dict[str, int]]) -> list[tuple[str, float]]:
    results = []
    for filename, keywords in db.items():
        similarity = 0
        for kw in kw_list:
            weight = calc_similarity(keywords, kw)
            similarity += weight
        results.append((filename, similarity))
    results.sort(key=get_count, reverse=True)
    return results

def print_results(results: list[tuple[str, float]]):
    for filename, similarity in results:
          print(f'{filename}: {similarity}')

if __name__ == '__main__':
    db = load_kewords('keywords.db')
    while True:
        kw_str = input('Search keywords:')
        kw_list = [kw.strip() for kw in kw_str.split(',')]
        results = search(kw_list, db)
        print_results(results)