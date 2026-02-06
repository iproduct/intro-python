def list_sum[E](l: list[E], zero_val: E = None) -> E:
    if not l:
        return zero_val
    return _list_sum(l[1:], type(l[0]))

def _list_sum[E](l: list[E], elem_type_ctor) -> E:
    return elem_type_ctor() if not l else l[0] + _list_sum(l[1:], elem_type_ctor)

if __name__ == '__main__':
    l1 = list(range(15))
    l2 = [chr(i + ord('a')) for i in range(15)]
    l3 = [[chr(i + ord('a'))] for i in range(15)]
    l4 = [(chr(i + ord('a')),) for i in range(15)]
    print(list_sum(l1))
    print(list_sum(l2))
    print(list_sum(l3))
    print(list_sum(l4))
