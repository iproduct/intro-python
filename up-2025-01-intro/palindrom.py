def is_palindrome(s: str) -> bool:
    s = s.lower().replace(' ', '')
    i = 0
    l = len(s) // 2
    while i <= l and s[i] == s[-i-1]:
        i += 1
    if i > l:
        return True
    return False

if __name__=="__main__":
    print(is_palindrome('Able was I ere I saw Elba'))