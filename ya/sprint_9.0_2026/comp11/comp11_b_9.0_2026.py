import sys


def f(n, corr_ans, st_ans1, st_ans2):
    cnt_match_corr_ans = cnt_match_incorr_ans = cnt_corr_ans = cnt_incorr_ans = 0
    for i in range(n):
        cnt_match_corr_ans += st_ans1[i] == st_ans2[i] and st_ans1[i] == corr_ans[i]
        cnt_match_incorr_ans += st_ans1[i] == st_ans2[i] and st_ans1[i] != corr_ans[i]
        cnt_corr_ans += st_ans1[i] == corr_ans[i]
        cnt_incorr_ans += st_ans1[i] != corr_ans[i]

    return cnt_match_corr_ans > .5 * cnt_corr_ans and cnt_match_incorr_ans > .5 * cnt_incorr_ans


def main():
    n = int(input())
    corr_ans = input()
    m = int(input())
    st_ans = [input() for _ in range(m)]

    ans = []
    for i in range(m):
        for j in range(i + 1, m):
            if f(n, corr_ans, st_ans[i], st_ans[j]) and f(n, corr_ans, st_ans[j], st_ans[i]):
                ans.append((i + 1, j + 1))
    
    print(len(ans))
    for a, b in ans:
        print(a, b)


if __name__ == '__main__':
    main()