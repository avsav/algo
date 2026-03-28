import sys


def f(n, a):
    sa = ''
    for i in range(1, n + 1):
        sa += str(i) 

    ans = n
    k = 0
    for _ in range(n):
        for i in range(n):
            if sa[i] == a[i]:
                k += 1
                break
            if i == n - 1 and sa[i] != a[i]:
                ans = k
                return ans
            
        a = int(a)
        a = str(a % 10) + str(a // 10)

        ans = min(ans, k)

    return -1


def main():
    n = int(input())
    a = input()
    a = ''.join(a.split())
    print(f(n, a))


if __name__ == '__main__':
    main()