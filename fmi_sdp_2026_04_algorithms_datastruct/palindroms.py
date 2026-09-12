import re

from profile_decorator import profile, profile_naive


# @profile
def is_palindrome(text: str) -> bool:
    regex = re.compile(r'\W+')
    normalized = regex.sub('', text).lower()
    if len(normalized) <= 1: # recursion bottom
        return True
    if normalized[0] == normalized[-1]: # recursion step
        return is_palindrome(normalized[1:-1])
    return False

def is_palindrome2(text: str) -> bool:
    regex = re.compile(r'\W+')
    normalized = regex.sub('', text).lower()
    return is_pal_rec(normalized)

# @profile
def is_pal_rec(text: str) -> bool:
    if len(text) <= 1: # recursion bottom
        return True
    if text[0] == text[-1]: # recursion step
        return is_pal_rec(text[1:-1])


@profile
def profile_is_palindrome(text: str):
    for _ in range(1000000):
        # is_palindrome2(text)
        is_pal_rec(text)

if __name__ == '__main__':
    # print(is_palindrome('Able was I, ere I saw Elba'))
    # print(profile_is_palindrome('Able was I, ere I saw Elba')) # True
    print(profile_is_palindrome('ablewasiereisawelba')) # True
