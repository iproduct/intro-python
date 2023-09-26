from profile_decorator import profile


def fact_gen(number):
    n = 1
    for i in range(1, number + 1):
        n *= i
        yield n


@profile
def test_fact_gen(n):
    s = 0
    for f in fact_gen(n):
        s += f
        # print(f)


if __name__ == '__main__':
    test_fact_gen(100000)
