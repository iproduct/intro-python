def remove_containing(str_set: set, str_to_remove):
    set_copy = str_set.copy()
    for element in set_copy:
        if str_to_remove in element:
            str_set.remove(element)

if __name__ == '__main__':
    str_set = set()
    while True:
        s = input('Enter a string [<Enter> for end]:')
        if s.strip() == '':
            break
        str_set.add(s)

    remove_containing(str_set, 'asd')
    print(str_set)

