from long_number import find_substitution


def test_find_substiution1():
    assert find_substitution(4, '1337', '1 2 5 4 6 6 3 1 9') == (1, 3, '1557')
def test_find_substiution2():
    assert find_substitution(5, '11111', '9 8 7 6 5 4 3 2 1') == (0, 5, '99999')
def test_find_substiution3():
    assert find_substitution(2, '33', '1 1 1 1 1 1 1 1 1') == (2, 2, '33')

