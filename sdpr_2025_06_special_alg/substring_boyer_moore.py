def find_substring_index_b_m(text, pattern):
    n, m = len(text), len(pattern)
    last = {}
    for i in range(m):
        last[pattern[i]] = i
    i = k = m - 1
    while i < n:
        print(f'i = {i}, k = {k}')
        print(text)
        print(' ' * (i - k) + pattern)
        if text[i] == pattern[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(text[i], -1)
            i += m - min(k, j + 1)
            k = m - 1
    return -1

if __name__ == '__main__':
    text = 'The reason we don’t just rely on setting entry’s pointer to nil'
    pattern = 'don'
    print(f'Indext of "{pattern}" in "{text} = {find_substring_index_b_m(text, pattern)}')