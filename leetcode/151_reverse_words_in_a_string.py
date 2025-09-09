# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=problem-list-v2&envId=nb4ro6ft


def reverseWords(s):
    s = s.split()
    n = len(s)
    for i in range(n//2):
        s[i], s[n - 1 - i] = s[n - 1 - i], s[i]
    return " ".join(s)


s1 = "the sky is blue"
s2 = "  hello world  "
s3 = "a good   example"
print(reverseWords(s3))