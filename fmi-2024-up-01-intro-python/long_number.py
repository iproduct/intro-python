
def create_f(subst_list):
    # return lambda n: subst_list[n - 1]
    def f(n):
        return subst_list[n - 1]
    return f

def find_index(predicate, iterable, start=0):
    last_index = 0
    for i, e in enumerate(iterable):
        last_index= i
        if i >= start and predicate(e):
            return i
    return last_index + 1

if __name__ == '__main__':
    a = list(map(int, input('Input a number:')))
    subst_list = list(map(int, input('Input f digit substitutions:')))
    f = create_f(subst_list)
    i = find_index(lambda d: f(d) > d, a)
    j = find_index(lambda d: f(d) < d, a, i+1)
    print(i, j)
    print(a[:i] + list(map(f, a[i:j])) + a[j:])