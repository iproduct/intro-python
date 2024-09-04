class A:
    def __init__(self):
        super().__init__()
        print('A')
    def __str__(self):
        return 'A'

class B:
    def __init__(self):
        super().__init__()
        print('B')
    def __str__(self):
        return 'B'

class C(A,B):
    def __init__(self):
        super().__init__()
        print('C')

if __name__ == '__main__':
    print(C.mro())
    c = C()
    print('__str__():', c)