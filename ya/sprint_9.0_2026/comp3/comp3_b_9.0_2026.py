import sys


def f(n):
    ans = n - 1
    for var in {n, 2*n - 1, 2*n, 2*n + 1}:
        for r in range(1, n + 1):
            if var % r == 0:
                if var == n:
                    m = var // r
                else:
                    m = (var // r + 1) // 2
                ans = min(ans, abs(r - m))

    return ans


def main():
    #n = int(input())
    n1 = 1 #output 0
    n2 = 2 #output 1
    n3 = 1 #output 0
    n4 = 50 #output 3
    print(f(n4))


if __name__ == '__main__':
    main()