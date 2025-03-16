# https://leetcode.com/problems/longest-palindromic-substring/description/

def longestPalindrome(s):
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    start = 0
    max_len = 1
    # l == 1
    for i in range(n):
        dp[i][i] = True
    # l == 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            if max_len < 2:
                start = i
                max_len = 2
    # l >= 3
    for l in range(3, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True
                if max_len < l:
                    start = i
                    max_len = l

    return s[start:start+max_len]


s1 = "babad"
s2 = "cbbd"
""" for i in longestPalindrome(s1):
    print(i) """
print(longestPalindrome(s2))