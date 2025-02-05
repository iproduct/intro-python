def dfs(tree: list | int) -> list[int]:
    if isinstance(tree, int):
        return [tree]
    childeren = tree[1:]
    leaves = []
    for child in childeren:
        leaves.extend(dfs(child))
    return leaves

def print_tree(tree: list | int, level = 0):
    if isinstance(tree, int):
        print(' ' * ((level-1 if level > 0 else 0)*2), '\u2515', '\u2501' * 1, end='', sep='')
        print(tree)
    else:
        print(' ' * ((level-1 if level > 0 else 0)*2), '\u2515', '\u2501' * 1, end='', sep='')
        print(f'{tree[0]}')
        childeren = tree[1:]
        for child in childeren:
            print_tree(child, level + 1)

if __name__ == "__main__":
    exp_tree = ['+',['*',['~',3], ['+', 2, 1]], ['-', 4, 5]]
    print(dfs(exp_tree))
    print_tree(exp_tree)