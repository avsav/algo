# https://leetcode.com/problems/longest-palindromic-substring/description/

def longestPalindrome(s):
    n = len(s)
    dp = [[False]*n for _ in range(n)]

    # l == 1
    for i in range(n):
        dp[i][i] = True
    # l == 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
    # l >= 3
    for l in range(3, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True

    return dp


s1 = "babad"
s2 = "cbbd"
for i in longestPalindrome(s1):
    print(i)