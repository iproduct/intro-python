def some_fun(a, b=10, *args, label='default', **kwargs):
    print('In a:', a)
    print('In b:', b)
    print('In label:', label)
    for i in args:
        print('In args:', i)
    for key, val in kwargs.items():
        print('In kwargs:', key, '=', val)

some_fun(1, 2, 3, 4, 5, type="Strings", name="Digits")

# def changer (x, y):
#     x = 2 # променя само локалната x
#     y[0] = 'hi'
#
# n = 5
# list = ['a', 'b', 'c']
#
# changer(n, list)
# print('n = ', n)
# print('list = ', list)