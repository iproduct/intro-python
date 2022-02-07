def f(a, b, /, c, *args, d, label='default', **kwargs):
    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("d =", d)
    print("*args =", args, " -> ", type(args))
    print("label =", label)
    print("**kwargs =", kwargs, " -> ", type(kwargs))

def my_print(*args, **kwargs):
    print("Positional: ", *args, sep=" | ")
    options = {"sep": " | ", "end": "...", "file": open("out.txt", "wt")}
    print("Keyword: ", *map(lambda kwarg: f"{kwarg[0]}:{kwarg[1]}", kwargs.items()), **options)


if __name__ == '__main__':
    f(1, 2, 3, 5, 6, 7, d=4, type="Strings", name="Digits", label='My Label')
    my_print(1, 2, 3, 5, 6, 7, d=4, type="Strings", name="Digits", label='My Label')
