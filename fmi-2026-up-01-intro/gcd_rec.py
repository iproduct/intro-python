
def gcd_rec(a,b):
    if b == 0:
        return a
    return gcd_rec(b,a%b)

if __name__ == '__main__':
    print(gcd_rec(354,606))
    print(gcd_rec(95,1025))