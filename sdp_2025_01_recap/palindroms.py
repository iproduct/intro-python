import re


def is_palindrome(text: str) -> bool:
    regex = re.compile(r'\W+')
    normalized = regex.sub('', text).lower();
    print(normalized)
    if len(normalized) <= 1: # recursion bottom
        return True
    if normalized[0] == normalized[-1]: # recursion step
        return is_palindrome(normalized[1:-1])
    # return normalized == normalized[::-1]


if __name__ == '__main__':
    print(is_palindrome('Able was I, ere I saw Elba')) # True
