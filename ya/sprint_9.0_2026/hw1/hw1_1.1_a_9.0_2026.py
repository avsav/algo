import sys


def f(p, v, q, m):
    a = p - v
    b = p + v
    c = q - m
    d = q + m
    n = 0
    if b < c:
        n = b - a + d - c + 2
    if d < a:
        n = d - c + b - a + 2
    if b == c or b > c and d > a:
        n = d - a + 1
    if d == a or d > a and b > c:
        n = b - c + 1
    if a < c and d < b:
        n = b - a + 1
    if c < a and b < d:
        n = d - c + 1
    return n


def main():
    #p, v = map(int, input().split())
    #q, m = map(int, input().split())
    p1, v1 = 0, 7
    q1, m1 = 12, 5
    p2, v2 = 1, 3
    q2, m2 = 6, 1
    print(f(p2, v2, q2, m2))


if __name__ == '__main__':
    main()