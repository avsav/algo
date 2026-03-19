import sys


def f(n, m, e, q):
    res = 0
    for l, r, x in e:
        if l <= q and q <= r:
            if l % 2 == q % 2:
                res += x
            else:
                res -= x
    return res


def main():
    n, m = map(int, input().split())
    e = [list(map(int, input().split())) for _ in range(n)]
    q = [int(input()) for _ in range(m)]
    for i in q:
        print(f(n, m, e, i))


if __name__ == '__main__':
    main()