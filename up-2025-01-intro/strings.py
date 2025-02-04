import random

sea = [
'00**0000',
'00**0**0',
'00000000',
'0******0',
'0*****00',
'0**0**00',
'00000000',
'00000000'
]

def print_sea(l: list[str]):
    for line in l:
        print(line)


if __name__ == "__main__":
    n = int(input("Enter N = "))
    print(f'Size: {n}')
    l = []
    for i in range(n):
        if 0 < i < n-1:
            s = '_'
            for j in range(1, n-1):
                s += '*' if random.random()  >= 0.5 else '_'
            s += '_'
            l.append(s)
        else:
            l.append('_' * n)

    print_sea(l)
    print()
    print_sea(sea)
