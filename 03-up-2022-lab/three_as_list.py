

tree = [['a', ['b', 'c'], 'd'], [['e', 'f', ['g', 'h', 'i'], ['j'], 'k'], 'l'], ['m', ['n', 'o']]]

# Depth-First Search(DFS)
def get_dfs_leaves(tree, results = None):
    if results == None:
        results = []
    if isinstance(tree, list): # recursion step - branch
        for elem in tree:
            get_dfs_leaves(elem, results)
    else:
        results.append(tree) #recursion bottom - leaf
    return results

if __name__ == "__main__":
    print(get_dfs_leaves(tree))