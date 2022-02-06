
if __name__ == '__main__':
    d = dict()
    keys = ["Sofia", "Plovdiv", "Varna"]
    temperatures = [2, 4, 6]
    z = zip(keys, temperatures)
    lz = list(z)
    print(lz)

    d = dict(lz)
    print(d)
    di = d.items()
    print(di)

    print(list(di))
    ruse_t = d.get("Ruse", -1)
    print(ruse_t)
    sofia_t = d.get("Sofia", -1)
    print(sofia_t)
    print(d['Sofia'])

    d.setdefault("Burgas")
    d.setdefault("Ihtiman", -2)
    print(d.setdefault("Burgas", -2))
    print(d.setdefault("Ihtiman", -4))
    # d["Burgas"] = -2
    # d["Ihtiman"] = -4
    print(d)
