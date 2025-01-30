def find_max_elem(l: list[int]) -> int:
    max = l[0]
    for i in range(1, len(l)): # iterate indexes of elements in  a sequence
        if l[i] > max:
            max = l[i]
    return max

def find_max_elem_index(l: list[int]) -> int:
    max = l[0]
    max_index = 0
    for i in range(1, len(l)): # iterate indexes of elements in  a sequence
        if l[i] > max:
            max = l[i]
            max_index = i
    return max_index

if __name__ == "__main__":
    l = [42, 456, 56, 78, 532, 94, 5, 234, 489, 12 ]
    print(find_max_elem(l))
    index = find_max_elem_index(l)
    print(f'{index} -> {l[index]}')