
def tree_sum(tree):
    sum = 0
    for elem in tree:
        if isinstance(elem, list): #branch
            sum += tree_sum(elem) # recursion step
        else: # leave
            sum += elem # recursion bottom
    return sum

if __name__ == '__main__':
    L = [1, [2, [3, 4], 5], 6, [7, 8]]
    print(tree_sum(L))