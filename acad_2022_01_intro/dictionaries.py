
if __name__ == "__main__":
    d1 = {frozenset({1, 2, 3}): 6, frozenset({'a', 'b', 'c'}): {frozenset({'abc'})}}
    print(d1)

    kv = zip(['a', 'c', 'd'], [1, 2, 3])
    d2 = dict(kv)
    print(list(zip(['a', 'c', 'd'], [1, 2, 3])))
    print(d2)
    print(d2.keys())
    print(d2.values())
    print(d2.items())
    d2.update({'b': 42, 'e': 18})
    print(d2)
    print(d2.popitem())
    print(d2)
    print(d2.popitem())
    print(d2)
    print(d2.pop('c'))
    print(d2)
    d2.update(f=42)
    # d2['a'] = 108
    print('setdefault =', d2.setdefault('a', 108))
    print(d2)

