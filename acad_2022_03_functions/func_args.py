
def f(x, y):
    x = 42
    y = (108, 2, 3)

def g(a,/, b, *, c, d="default", e, **kwargs):
    print(a,  b,  c, d, e, kwargs)

if __name__=="__main__":
    a = 12
    b = (1, 2, 3)
    f(a, b)
    print(a, b)
    g(42, b=512, f=123, e=123, c=321, g="def", h="xyz", format="long")
