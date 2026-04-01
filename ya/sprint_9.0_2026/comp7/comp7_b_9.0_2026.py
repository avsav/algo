import sys


def f(n, types):
    ans = 0
    n = len(types)
    ans = max_len = 0
    d = {}
    for i in range(n):
        d[types[i]] = d.get(types[i], 0) + 1
        cnts = [*d.values()]
        if len(cnts) >= 2:
            max_len = cnts[-1] + cnts[-2]
        ans = max(ans, max_len)
    return ans


def main():   
    n = int(input())
    types = list(map(int, input().split()))
    print(f(n, types))


if __name__ == '__main__':
    main()