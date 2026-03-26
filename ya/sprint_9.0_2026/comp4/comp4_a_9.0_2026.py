import sys


def f(n, names, scores):
    ans = 0
    a0 = b0 = 0
    for s in scores:
        a1, b1 = map(int, s[0].split(':'))
        t = s[1]
        names[t] = names.get(t) + a1 - a0 + b1 - b0
        a0, b0 = a1, b1
    ans = max(names.items(), key=lambda n: n[1])
    
    return ans[0] + " " + str(ans[1])


def main():
    n = int(input())
    names = {input():0 for _ in range(n)}
    m = int(input())
    scores = [input().split() for _ in range(m)]
    print(f(n, names, scores))


if __name__ == '__main__':
    main()