import math
from math import floor

if __name__ == '__main__':
    for c in range(ord('a'), ord('z')+1):
        print(chr(c), sep='|', end='|')
    l = ['Hello', 'Wonderful', 'Python', 'World']
    print('\n', str(l))
    print(' | '.join(l))

    print('%12.4f, %12d, %s' % (math.pi, math.e, l))
    print('{0:6.4f}, {1:6.4f}, {2:10.10s}'.format(math.pi, math.e, str(l)))
    print(f'{math.pi:6.4f}, {math.e:6.4f}, {str(l):10.10s}')

    lengths = []
    for elem in l:
        lengths.append(len(elem))
    print(lengths)

    print(f'Sum={sum(lengths)}')
    print(f'Max word length={max(lengths)}')
    print(*lengths, sep=' | ')
    print(f'Max word length={max(*lengths)}')
    print(math.ceil(4))


