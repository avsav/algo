# https://leetcode.com/problems/combinations/description


def combine(n, k):
    comb = []
    res = []

    def backtrack(i):
        if len(comb) == k:
            res.append(comb.copy())
            return
        if i <= n:
            comb.append(i)
            backtrack(i + 1)
            comb.pop()
            backtrack(i + 1)

    backtrack(1)

    return res




n1 = 4
k1 = 2
n2 = 1
k2 = 1
print(combine(n2, k2))