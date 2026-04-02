import sys


def main():
    cases = int(input())
    for c in range(cases):
        n, d = map(int, input().split())
        ans = 1
        curr_d = d
        for i in range(1, n + 1):
            t, k = map(int, input().split())
            if curr_d > t:
                ans = i + 1
            curr_d += k

        print(ans)


if __name__ == '__main__':
    main()