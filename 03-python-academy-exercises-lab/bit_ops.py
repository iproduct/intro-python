import enum

if __name__ == '__main__':
    x = 127
    y = x & 3
    print('x=', f'{x:08b}')
    print('y=', f'{y:08b}')
    l = ["a", "b", "c"]
    i = 0
    while i < len(l):
        print(i, " -> ", l[i])
        i += 1

    for i in range(len(l)):
        print(i, " -> ", l[i])

    for i, v in enumerate(l):
        print(i, " -> ", v)

    print(list(range(len(l))))
    print(list(enumerate(l)))

    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

    newlist = [x for x in fruits if "a" in x]
    newtuple = tuple([x for x in fruits if "a" in x])
    newset = {x  for x in fruits if "a" in x}
    newdict = {x : len(x) for x in fruits if "a" in x}

    print(newlist)
    print(newtuple)
    print(newset)
    print(newdict)

    [print(chr(utf), end="") for utf in range(0x1F500, 0x1F700)]