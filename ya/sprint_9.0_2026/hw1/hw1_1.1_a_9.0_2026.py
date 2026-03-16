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
    if b == c:
        n = d - a + 1
    if d == a:
        n = b - c + 1
    if b > c and d > b and c > a:
        n = d - a + 1
    if d > a and b > d and a > c:
        n = b - c + 1
    if a < c and d < b:
        n = b - a + 1
    if c < a and b < d:
        n = d - c + 1
    return n


def main():
    #p, v = map(int, input().split())
    #q, m = map(int, input().split())
    p1, v1, q1, m1 = 0, 7, 12, 5                    #output 25
    p2, v2, q2, m2 = 1, 3, 6, 1
    p3, v3, q3, m3 = -10**8, 10**8, 10**8, 10**8
    p4, v4, q4, m4 = -1, 12, 8, 17                  #output 39
    print(f(p4, v4, q4, m4))


if __name__ == '__main__':
    main()