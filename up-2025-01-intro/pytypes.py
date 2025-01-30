import math

if __name__ == '__main__':
    for c in range(ord('a'), ord('z')+1):
        print(chr(c), sep='|', end='|')
    l = ['Hello', 'Python', 'World']
    print('\n', str(l))
    print(' | '.join(l))
    print('%12.4f, %12d, %s' % (math.pi, math.e, l))
    print('{0:6.4f}, {1:6.4f}, {2:10.10s}'.format(math.pi, math.e, str(l)))
    print(f'{math.pi:6.4f}, {math.e:6.4f}, {str(l):10.10s}')

