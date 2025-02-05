from collections.abc import Iterable


def is_palindrome(s: str) -> bool:
    s = s.lower().replace(' ', '')
    i = 0
    l = len(s) // 2
    while i <= l and s[i] == s[-i-1]:
        i += 1
    if i > l:
        return True
    return False

def print_enum(s: Iterable):
    for i, v in enumerate(s):
        print(f'{i}, {v}')

if __name__=="__main__":
    print(is_palindrome('Able was I ere I saw Elba'))
    print_enum('Able was I ere I saw Elba')
    print()
    print_enum('Able was I ere I saw Elba'.split(' '))
