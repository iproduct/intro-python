def find_index(lst, elem):
    for i in range(len(lst)):
        if elem == lst[i]:
            return i
    return None


if __name__ == '__main__':
    l = ['abcd', 'hi', 'def', 'aaa', 'addsa']
    ind = find_index(l, 'aaab')
    print(f'{ind} -> {l[ind]}' if ind is not None else 'Element not found')