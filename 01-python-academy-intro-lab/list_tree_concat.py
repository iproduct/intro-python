
tree = ["a",["b",[["c"], ["d", "e"]], "f"], ["g", ["h", ["l", "m"], "n"]]] # expected: "abcdefghlmn"

# depth first traversal
def depth_first_concat(tree_as_list):
    pass