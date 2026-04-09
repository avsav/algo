# https://coderun.yandex.ru/selections/algorithm-training-september-2025/problems/ball-on-the-stairs


import sys


def f1(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    return f1(n - 1) + f1(n - 2) + f1(n - 3)


def f2(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    
    prev1 = 1
    prev2 = 2
    curr = 4
    for i in range(4, n + 1):
        tmp = curr
        curr = prev1 + prev2 + curr
        prev1 = prev2
        prev2 = tmp

    return curr


def main():
    n = int(input())
    print(f1(n))
    print(f2(n))


if __name__ == '__main__':
    main()