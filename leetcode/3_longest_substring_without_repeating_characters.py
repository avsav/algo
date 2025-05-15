# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

def lengthOfLongestSubstring(s):
    n = len(s)
    m = set()
    l = maxLen = 0
    for r in range(n):
        while s[r] in m:
            m.remove(s[l])
            l += 1
        m.add(s[r])
        maxLen = max(maxLen, r - l + 1)

    return maxLen


s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
s4 = " "
print(lengthOfLongestSubstring(s4))