from functools import reduce


def f_x(x):
    if segment[x] > int(x):
        return str(segment[x])
    return x


if __name__ == "__main__":
    n = int(input())
    a = list(input().strip())
    segment = dict(zip([str(i) for i in range(1, 10)], map(int, input().split())))

    print(reduce(lambda x, y: x + f_x(y), a, ''))