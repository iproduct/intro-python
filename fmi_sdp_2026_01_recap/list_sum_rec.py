def list_sum_rec(lst):
    if lst == []:
        return 0
    return lst[0] + list_sum_rec(lst[1:])

def list_sum_rec(lst):
    if lst == []:
        return 0
    if not isinstance(lst, list):
        return lst
    return list_sum_rec(lst[0]) + list_sum_rec(lst[1:])

if __name__ == '__main__':
    print(list_sum_rec([]))
    print(list_sum_rec([12, 43, 7, 55, 17]))
    print(list_sum_rec([[12, [43, 7]], [55, [[17,[9]]]], 12]))