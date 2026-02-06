def list_sum[E](l: list[E], zero_val: E = None) -> E:
    if not l:
        return zero_val
    return _list_sum(l[1:], type(l[0]))

def _list_sum[E](l: list[E], elem_type_ctor) -> E:
    return elem_type_ctor() if not l else l[0] + _list_sum(l[1:], elem_type_ctor)

def tree_list_sum[E](l: list[E | list[E]], zero_val: E = None) -> E:
    if not l:
        return zero_val
    return _tree_list_sum(l[1:], get_leaf_type(l))

def _tree_list_sum[E](l: list[E], elem_type_ctor) -> E:
    if not type(l) is list:  # l is a leaf of type E
        return l
    if not l:
        return elem_type_ctor()  # zero value for type E
    return _tree_list_sum(l[0], elem_type_ctor) + _tree_list_sum(l[1:], elem_type_ctor)

def get_leaf_type[E](l: list[E | list[E]]) -> type[E]:
    if not l:
        return None
    if not type(l) is list:  # l is a leaf of type E
        return type(l)
    for e in l:
        t = get_leaf_type(e)
        if t is not None:
            return t
        return None

if __name__ == '__main__':
    l1 = list(range(15))
    l2 = [chr(i + ord('a')) for i in range(15)]
    l3 = [[chr(i + ord('a'))] for i in range(15)]
    l4 = [(chr(i + ord('a')),) for i in range(15)]
    print(list_sum(l1))
    print(list_sum(l2))
    print(list_sum(l3))
    print(list_sum(l4))

    tree = [1, [2, [3, 4], 5], 6, [7, 8]]
