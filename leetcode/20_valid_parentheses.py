# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(":")", "{":"}", "[":"]"}
        for symb in s:
            if symb in pairs.keys():
                stack.append(symb)
            else:
                open_bracket = stack.pop()
                if pairs[open_bracket] == symb:
                    stack.pop()
        return len(stack) == 0 
    

obj = Solution()
s = input("Введите строку: ")
print(obj.isValid(s))