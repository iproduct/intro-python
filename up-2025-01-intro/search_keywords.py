from keywords import print_file_keywords


def load_kewords(dbfilename: str) -> dict[str, list[tuple[str, int]]]:
    results = {}
    with open(dbfilename) as db:
        for line in db:
            parts = line.split(',')
            filename = parts[0]
            keywords = []
            for word_count in parts[1:]:
                word, count = word_count.split(':')
                keywords.append((word, int(count)))
            results[filename] = keywords
    return results

if __name__ == '__main__':
    db = load_kewords('keywords.db')
    print_file_keywords(db)