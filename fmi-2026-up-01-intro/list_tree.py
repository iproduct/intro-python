
def find_max_leaf(tree_as_list):
    def process(tree):
        if not isinstance(tree, list): # recursion bottom - leaf
            return tree
        # recursion step - subtree
        max = None
        for subtree in tree:
            val = process(subtree)
            if max is None or val > max:
                max = val
        return max
    return process(tree_as_list)

if __name__ == '__main__':
    tree = [[7,3], [[[8,11], 5], 17], 9]
    print(find_max_leaf(tree))