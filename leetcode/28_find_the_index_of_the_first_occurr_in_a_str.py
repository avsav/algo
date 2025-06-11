# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

def strStr(haystack, needle):
    # Naive string matcher
    h = len(haystack)
    n = len(needle)
    if h < n:
        return -1
    res = 0
    for i in range(h - n + 2):
        for j in range(n):
            k = i + j
            if k == h:
                k -= 1
            if needle[j] != haystack[k]:
                res = -1
                break
            if j == n - 1:
                res = i
                return res

    return res


haystack1 = "sadbutsad"
needle1 = "sad"
haystack2 = "leetcode"
needle2 = "leeto"
haystack3 = "mississippi"
needle3 = "a"
haystack4 = "mississippi"
needle4 = "sippia"
print(strStr(haystack4, needle4))