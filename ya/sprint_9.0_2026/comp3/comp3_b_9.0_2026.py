import sys


def f(n):
    ans = n - 1
    for var in {n, 2*n - 1, 2*n, 2*n + 1}:
       r = 1
       while r * r <= var:
            if var % r == 0:
                if var == n:
                    m = var // r
                else:
                    m = (var // r + 1) // 2
                ans = min(ans, abs(r - m))
            r += 1
    return ans


def main():
    #n = int(input())
    n1 = 1 #output 0
    n2 = 2 #output 1
    n3 = 1 #output 0
    n4 = 50 #output 3
    print(f(n1))


if __name__ == '__main__':
    main()