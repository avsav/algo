import sys


def f(n, s):
    ans = cnt = 0
    for i in range(n):
        if i == 0 and s[i] in "ah":
            cnt = 1
        if i >= 1:
            if s[i - 1] == "a" and s[i] == "h" or s[i - 1] == "h" and s[i] == "a":
                cnt += 1
            else:
                cnt = 0
            if s[i] in "ah" and (s[i - 1] == s[i] or s[i - 1] not in "ah"):
                cnt = 1
        ans = max(ans, cnt)
    return ans


def main():
    #n = int(input())
    #s = input()
    n1 = 6
    s1 = "aaahhh" #output 2
    n2 = 5
    s2 = "ahaha" #output 5
    n3 = 24
    s3 = "ahahrunawayahahsofasthah" #output 4
    n4 = 10
    s4 = "ahahaahaha" #output 5
    n5 = 2
    s5 = "bb"
    print(f(n1, s1))


if __name__ == '__main__':
    main()