def log_factory():
    _history = []

    def log(pos):
        _history.append(pos)
        return _history

    return log


def append2(x, list2=None):
    if list2 is None:
        list2 = []
    list2.append(x)
    return list2  # effectively immutable


if __name__ == "__main__":
    # l1 = append1(1)
    veh1 = log_factory()
    veh2 = log_factory()
    print(veh1((202, 105)))
    print(veh1((203, 105.8)))
    print(veh2((204, 106.3)))
    print(veh2((205, 107)))
    a2 = append2(1)
    print(a2)
    a2.append(42)
    print(append2(2, a2))
