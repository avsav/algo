# https://coderun.yandex.ru/selections/algorithm-training-september-2025/problems/ball-on-the-stairs


import sys


def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    return f(n - 1) + f(n - 2) + f(n - 3)


def main():
    n = int(input())
    print(f(n))


if __name__ == '__main__':
    main()