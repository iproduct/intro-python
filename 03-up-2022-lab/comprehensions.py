
if __name__ == '__main__':
    # list comprehensions
    listcomp = [x * x for x in range(1, 11) if x % 2 == 0]
    print(listcomp)
    listcomp_str = [x.upper() for x in "I like Python!" if x.isalpha()]
    print(listcomp_str)

    # dict comprehensions
    dictcomp = {x: x * x for x in range(1, 11) if x % 2 == 0}
    print(dictcomp)
    dictcomp_str = {x.upper(): len(x) for x in "I like Python !".split() if len(x) > 1}
    print(dictcomp_str, type(dictcomp_str))

    # set comprehension
    setcomp_str = {x.upper() for x in "I like Python!" if x.isalpha()}
    print(setcomp_str, type(setcomp_str))

    # generator comprehension
    gencomp_str = (x.upper() for x in "I like Python!" if x.isalpha())
    print(gencomp_str, type(gencomp_str))
    # print(list(gencomp_str))
    # print(set(gencomp_str))
    print(tuple(gencomp_str))

    # generator comprehension
    tuplecomp_str = *(x.upper() for x in "I like Python!" if x.isalpha()),
    print(tuple(tuplecomp_str))






