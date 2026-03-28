import sys


def f(n, a):
    ans = 0
    for _ in range(n):
        if all(a[i] != i + 1 for i in range(n)):
            return ans
        else:
            ans += 1
        last = a.pop()
        a.insert(0, last)

    return -1


def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    print(f(n, a))


if __name__ == '__main__':
    main()