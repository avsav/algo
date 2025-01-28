# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

""" 
class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(" ")
        res = ""
        for w in l:
            res += w[::-1]
            res += " "
        l = len(res) - 1
        return res[:l]
"""