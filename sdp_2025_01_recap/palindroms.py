import re

from profile_decorator import profile
from trace import trace



@profile
# @trace
def is_palindrome(text: str) -> bool:
    regex = re.compile(r'\W+')
    normalized = regex.sub('', text).lower()
    if len(normalized) <= 1: # recursion bottom
        return True
    if normalized[0] == normalized[-1]: # recursion step
        return is_palindrome(normalized[1:-1])
    # return normalized == normalized[::-1]

@profile
def profile_is_palindrome(text: str):
    for _ in range(1000):
        is_palindrome(text)

if __name__ == '__main__':
    print(profile_is_palindrome('Able was I, ere I saw Elba')) # True
    print(is_palindrome.__name__)
