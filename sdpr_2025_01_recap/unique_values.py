if __name__ == '__main__':
    d = {}
    while True:
        inp = input('Input <key>, <value> [<Enter> to finish]:')
        if inp == '':
            break
        key, value = inp.split(',')
        key = key.strip()
        value = value.strip()
        d[key] = value
    values = set(d.values())
    print(values)