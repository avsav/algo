import sys


def f(n, words):
    words.sort()
    m = len(words[0])
    ans = m
    for i in range(0, n, 2):
        j = k = 0
        while j < m and words[i][j] == words[i + 1][j]:
            k += 1
            j += 1
        ans = min(ans, k)
 
    return ans


def main():
    n = int(input())
    words = [input() for _ in range(n)]
    print(f(n, words))


if __name__ == '__main__':
    main()