from typing import Callable


def find_in_tree[E](numbers_tree_list: list[E | list[E]], predicate: Callable[[E], bool]) -> E | None:
    ...


if __name__ == "__main__":
    t1 = [1, [2, [3, 4], 5], 6, [7, 8]]
    print(find_in_tree(t1, lambda x: x % 3 == 0))