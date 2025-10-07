if __name__ == '__main__':
    s = input('Input a string: ')
    # 1
    print(s[0:2] + s[-2:])
    mid_index = len(s) // 2
    print(s[0] + s[mid_index] + s[-1])
    print(s[mid_index - 1: mid_index + 2] )
    # 2
    first_char = s[0]
    print(s.replace(first_char, '$'))
    print(first_char + s[1:].replace(first_char, '$'))
    # 3
    strings = s.split(',')
    s1 = strings[0].strip()
    s2 = strings[1].strip()
    print(s2[0:2] + s1[2:] + ' ' + s1[0:2] + s2[2:])
