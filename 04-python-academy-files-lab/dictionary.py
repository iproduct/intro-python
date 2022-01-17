if __name__ == "__main__":
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    thisdict["hp"] = 2400
    thisdict["owner"] = 'John Smith'

    for i, x in enumerate(thisdict):
        print(i, '->', x, '->', thisdict[x])

    myfamily = {
        frozenset(["a", "child1"]): {
            "name": "Emil",
            "year": 2004
        },
        frozenset(["b", "child2"]): {
            "name": "Tobias",
            "year": 2007
        },
        frozenset(["c", "child3"]): {
            "name": "Linus",
            "year": 2011
        }
    }

    for k in myfamily:
        print(k, '->', myfamily[k])

    x = range(10)

    thisdict = dict.fromkeys(x, 1)
    print(thisdict)

    thisdict2 = {item: item**2 for item in x if item%2 == 0}

    print(thisdict2)