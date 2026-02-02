import copy

def keyfunc_value(tup):
    return str(tup[1]).lower()

if __name__ == '__main__':
    keys = ["streetAddress", "city", "state", "postalCode"]
    values = ["21 2nd Street", "New York", "NY", 10021]
    kv_iterable = zip(keys, values)
    # for k, v in kv_iterable:
    #     print(f'{k:14} : {v}')
    dictionary = dict(kv_iterable)
    print(dictionary)
    keyset = set(dictionary.keys())
    print(keyset)
    print("city" in keyset)
    items = dictionary.items()
    itemlist = list(items)
    itemlist.sort(key=keyfunc_value)
    print(itemlist)

    original = {"a": [1, 2, 3], "b": {"c": 4}}
    for k in original:
        print(k, ' ->', original[k])
    # copied_dict = original.copy() # shallow copy
    copied_dict = copy.deepcopy(original) # deep copy
    original['a'][0] = 42
    print(original)
    print(copied_dict)

    while original:
        item = original.popitem()
        print(item)
    print(original)
