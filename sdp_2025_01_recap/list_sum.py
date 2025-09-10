from typing import Union


def list_sum(l : list[int]) -> int:
    pass # TODO implemetation

type IntTree = list[Union[int, IntTree]]

def tree_sum(t : IntTree) -> int:
    if isinstance(t, int):
        return t
    elif isinstance(t, list):
        total = 0
        for node in t:
            total += tree_sum(node)
        return total
    else:
        raise TypeError('t must be an int or list')

if __name__ == '__main__':
    s = tree_sum([2,[17,8],[5,[4],1],9])
    print(s)