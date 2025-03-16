# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

def findAnagrams(s, p):
    ls = len(s)
    lp = len(p)
    sorted_p = "".join(sorted(p))
    res = []
    i = 0
    while i + lp <= ls:
        sorted_str = "".join(sorted(s[i:i+lp]))
        if sorted_str == sorted_p:
            res.append(i)
        i += 1
    return res


s1 = "cbaebabacd"
p1 = "abc"
s2 = "abab"
p2 = "ab"
s3 = "eklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpy"
p3 = "yqrbgjdwtcaxzsnifvhmou"
print(findAnagrams(s3, p3))