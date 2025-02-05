def find_indices(s: str, keyword: str) -> list[int]:
    start = 0
    indices = []
    while True:
        i = s.find(keyword, start)
        if i < 0:
            break
        indices.append(i)
        start = i + 1
    return indices

if __name__ == '__main__':
    s = """
    Guido van Rossum began working on Python in the late 1980s as a successor to the 
    ABC programming language and first released it in 1991 as Python 0.9.0.[36] 
    Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major 
    revision not completely backward-compatible with earlier versions. 
    Python 2.7.18, released in 2020, was the last release of Python 2
    """
    keyword = 'Python'
    indices = find_indices(s, keyword)
    for i in indices:
        print(f'{s[i:i + len(keyword)]} -> {i}')