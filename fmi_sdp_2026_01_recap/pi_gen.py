import math

def squares_gen(n):
    for i in range(1, n+1):
        yield i*i

def pi_gen_leibniz(n):
    sum, sign = 0, 1
    for i in range(n):
        sum += sign * 4 / (2*i + 1)
        sign *= -1
        yield sum

def pi_gen_euler(n):
    sum = 0
    for sq in squares_gen(n):
        sum += 6 / sq
        yield math.sqrt(sum)

if __name__ == '__main__':
    print(math.pi)
    for i in pi_gen_leibniz(5000):
        print(i)
    print("diff:", math.pi - i,"\n\n\n")
    for i in pi_gen_euler(5000):
        print(i)
    print("diff:", math.pi - i)
