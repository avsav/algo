# https://leetcode.com/problems/generate-parentheses/description/


def generateParenthesis1(n):
    res = []
    left = right = 0
    stack = [(left, right, "")]

    while stack:
        left, right, s = stack.pop()
        if len(s) == 2 * n:
            res.append(s)
        if left < n:
            stack.append((left + 1, right, s + "("))
        if left > right:
            stack.append((left, right + 1, s + ")"))

    return res


def generateParenthesis2(n):

    def dfs(left, right, s):
        if len(s) == 2 * n:
            res.append(s)
            return
        if left < n:
            dfs(left + 1, right, s + "(")
        if left > right:
            dfs(left, right + 1, s + ")")
            
    res = []
    dfs(0, 0, "")

    return res


n = int(input())
print(generateParenthesis1(n))
print(generateParenthesis2(n))