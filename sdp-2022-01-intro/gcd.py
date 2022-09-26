if __name__ == '__main__':
    a = int(input("First number A:"))
    b = int(input("First number B:"))


    def gcd(a: int, b: int) -> int:
        while b > 0:
            a, b = b, a % b
            # print(a, b)
        return a


    def gcd_rec(a: int, b: int) -> int:
        return a if b == 0 else gcd(b, a % b)


    print(f'A={a}, B ={b}, GCD={gcd_rec(a, b)}')
