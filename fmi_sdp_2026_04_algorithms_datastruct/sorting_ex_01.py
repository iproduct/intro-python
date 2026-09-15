from typing import List


def sort_bubble(lst: List[int | float]):
    n = len(lst) - 1
    swapped = True
    while n > 0 and swapped:
        swapped = False
        for i in range(n):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
        n -= 1

def find_min_index(lst: List[int | float], begin: int = 0, end: int = None) -> int:
    if end is None:
        end = len(lst)
    i = begin
    min_val = lst[begin]
    min_index = begin
    while i < end:
        if lst[i] < min_val:
            min_val = lst[i]
            min_index = i
        i += 1
    return min_index


def sort_selection_min(lst: List[int | float]) -> None:
    n = len(lst)
    for k in range(n-1):
        min_index = find_min_index(lst, k, n)
        lst[k], lst[min_index] = lst[min_index], lst[k]


if __name__ == "__main__":
    lst = [45, 667, 12, 34, 67, 12, 5, 17, 8]
    # sort_bubble(lst)
    sort_selection_min(lst)
    print(lst)
