import sys


def f(n, xd):
    ans = 0

    for p in xd:
        a = p[0] - p[1]
        b = p[0] + p[1]
        p[0] = a
        p[1] = b

    a0, b0 = xd[0][0], xd[0][1]
    for a, b in xd:
        a = max(a, a0)
        b = min(b, b0)
        if a <= b:
            ans = b
        else:
            return -1
        a0 = a
        b0 = b

    return ans


def main():
    n = int(input())
    xd = [list(map(int, input().split())) for _ in range(n)]
    print(f(n, xd))


if __name__ == '__main__':
    main()