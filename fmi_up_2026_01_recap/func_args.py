def f(a,b,/,c, d, *args, e = None, f = None, g = None, **kwargs):
    print(a,b,c,d,e,f, g)
    print(args)
    print(kwargs)

if __name__ == '__main__':
    f(1,2,3,4, 101,102,103,h=8, i= 9, j = 10, e= 5,f=6,g=7)