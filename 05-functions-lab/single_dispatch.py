from functools import singledispatch


@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)


@fun.register(int)
def _(arg, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)


@fun.register
def _(arg: list, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)

if __name__ == '__main__':
    fun("Hello, world.", verbose=True)
    fun(42, verbose=True)
    fun(['spam', 'spam', 'eggs', 'spam'], verbose=True)
