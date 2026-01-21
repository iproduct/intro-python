
if __name__ == "__main__":
    s = "Hello World"
    # s[1] = "a" # doesn't work - string is immutable
    letters = list(s)
    print(letters)
    letters[1] = "a" # works! - list is mutable
    reversed_letters = letters[::-1] # reverse list
    s2 = ''.join(reversed_letters)
    print(s2)

    codes = bytearray(s, 'utf-8')
    print(codes)
    codes[1] = ord('a') # works! - bytearray is mutable
    s3 = codes.decode(encoding='utf-8')
    print(s3)

