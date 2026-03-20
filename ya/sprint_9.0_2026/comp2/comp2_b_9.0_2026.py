import sys


def f(n, m, h, w):
    ans = 0
    while n > h:
        h *= 2
        ans += 1
    while m > w:
        w *= 2
        ans += 1

    return ans


def main():
    n, m, h, w = map(int, input().split())
    print(min(f(n, m, h, w), f(m, n, h, w)))


if __name__ == '__main__':
    main()