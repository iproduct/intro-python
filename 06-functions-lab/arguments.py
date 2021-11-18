def some_fun(name, /, pos_or_keyword, *a, content, **b):
    print("Positional args:\n", name, "\n", pos_or_keyword, sep="")
    for i in a:
        print(i)
    print("\nKeyword args:\n", content, sep="")
    for key, val in b.items():
        print(key, "->", val)

if __name__ == "__main__":
    some_fun("trayan", 1, 2, 3, pos = "the default", content = "My content ...", title="Digits", sep=", ", )
