
if __name__ == "__main__":
    s = "Hello World"
    # s[1] = "a" # doesn't work - string is immutable
    letters = list(s)
    print(letters)
    letters[1] = "a" # works! - list is mutable
    reversed_letters = letters[::-1] # reverse list
    s2 = ''.join(reversed_letters)
    print(s2)