from mpmath import mp

mp.dps = 500
mp.pretty = True

def calculate_pi(n):
    percent = n / 100
    acc = mp.mpf(0)
    for i in range(n):
        if i % percent == 0:
            print(chr(0x25A9), sep="", end="")
        acc += 4.0 * (1 - (i % 2) * 2) / (2 * i + 1)
    return acc


if __name__ == '__main__':
    print("\n", calculate_pi(10000000))
