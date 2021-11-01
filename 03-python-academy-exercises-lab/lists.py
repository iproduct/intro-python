import enum
import sys

if __name__ == '__main__':
    l = ["a", "b", "c"]
    i = 0
    while i < len(l):
        print(i, " -> ", l[i])
        i += 1
    print()

    for i in range(len(l)):
        print(i, " -> ", l[i])
    print()

    for i, v in enumerate(l):
        print(i, " -> ", v)
    print()

    print(list(range(len(l))))
    print(list(enumerate(l)))

    fruits = ["apple", "banana", "cherry", "kiwi", "mango", "orange", "papaya", "pineaple"] * 5

    newlist = [x for x in fruits if "a" in x]
    newtuple = *(x for x in fruits if "a" in x),
    newset = {x  for x in fruits if "a" in x}
    newdict = {x : len(x) for x in fruits if "a" in x}
    generator = (x for x in fruits if "a" in x)
    enumeration = enumerate(newlist)
    range_len = range(len(newlist))

    print(newlist, "->", sys.getsizeof(newlist), "bytes")
    print(newtuple, "->", sys.getsizeof(newtuple), "bytes")
    print(newset, "->", sys.getsizeof(newset), "bytes")
    print(newdict, "->", sys.getsizeof(newdict), "bytes")
    print(generator, "->", sys.getsizeof(generator), "bytes")
    print(enumeration, "->", sys.getsizeof(enumeration), "bytes")
    print(range_len, "->", sys.getsizeof(range_len), "bytes")

    #UTF32
    [print(chr(utf), end="") for utf in range(0x1F500, 0x1F7EA)]
    print()
    print("\U0001F7EA" * 60)