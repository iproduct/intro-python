def reverse_str(s):
    result = ''
    for ch in s:
        result = ch + result
    return result

if __name__ == '__main__':
    print(reverse_str('hello'))
    print(reverse_str('world'))