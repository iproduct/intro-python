from typing import Union


def list_sum(l : list[int]) -> int:
    pass # TODO implemetation

type IntTree = list[Union[int, IntTree]]

def list_sum(t : IntTree) -> int:
    if isinstance(t, int):
        return t
    elif isinstance(t, list):
        total = 0
        for node in t:
            total += list_sum(node)
        return total
    else:
        raise TypeError('t must be an int or list')

if __name__ == '__main__':
    s = list_sum([2,[17,8],[5,[4],1],9])
    print(s)