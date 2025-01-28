# https://leetcode.com/problems/valid-palindrome/description/

""" 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphnum = ""
        for i in range(len(s)):
            if s[i].isalnum():
                alphnum += s[i]
        alphnum = alphnum.lower()

        return alphnum == alphnum[::-1]
"""