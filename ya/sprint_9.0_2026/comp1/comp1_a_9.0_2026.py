import sys


def f(n, m, a):
    res = 0
    for i in range(n):
        for j in range(m):
            if j + 1 < m and a[i][j] == "." and a[i][j + 1] == ".":
                res += 1
            if i + 1 < n and a[i][j] == "." and a[i + 1][j] == ".":
                res += 1
    return res


def main():
    n, m = map(int, input().split())
    a = [input() for _ in range(n)]
    print(f(n, m, a))


if __name__ == '__main__':
    main()