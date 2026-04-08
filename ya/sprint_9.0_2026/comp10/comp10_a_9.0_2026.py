import sys


def f(n, m, photo):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if photo[i][j] == "#":
                if (j == 0 or photo[i][j - 1] == ".") and (i == 0 or photo[i - 1][j] == "."):
                    cnt += 1
    
    return cnt


def main():
    n, m = map(int, input().split())
    photo = [input() for _ in range(n)]
    print(f(n, m, photo))


if __name__ == '__main__':
    main()