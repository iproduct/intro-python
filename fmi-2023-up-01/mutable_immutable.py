if __name__ == '__main__':
    s = 'def' # immutable
    s2 = s + 'g'
    print(s2 is s)
    print(s)
    print(s2)

    l2 = l = ['a', 'b', 'c'] #mutable
    l.append('d')
    print(l2 is l)
    print(l)
    print(l2)

    t = ('a', 'b', 'c') #immutable
    t2 = t + ('d',)
    print(t2 is t)
    print('t:', t, ' -> ', id(t))
    print('t2:', t2, ' -> ', id(t2))

    s2 = s = {'a', 'b', 'c'} #mutable
    s.add('d',)
    print(s2 is s)
    print('s:', s, ' -> ', id(s))
    print('s2:', s2, ' -> ', id(s2))
