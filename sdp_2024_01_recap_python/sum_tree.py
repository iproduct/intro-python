def sum_tree(l):
    sum = 0
    if isinstance(l, list):
        for i in l:
            sum += sum_tree(i)
    else:
        sum = l
    return sum

if __name__ == '__main__':
    L = [1, [2, [3, 4], 5], 6, [7, 8]]
    print(sum_tree(L))
