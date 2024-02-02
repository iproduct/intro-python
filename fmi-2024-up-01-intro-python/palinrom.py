


if __name__ == '__main__':
    ls = ['Liver', 'Level', 'Racecar', 'Racer']
    for s in ls:
        s = s.lower()
        rev = s[::-1]
        print(f'{s} -> {rev} , Palindrom: {s == rev}')