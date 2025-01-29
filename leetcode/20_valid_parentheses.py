# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(":")", "{":"}", "[":"]"}
        for symb in s:
            if symb in pairs.keys():
                stack.append(symb)
            elif not stack and symb not in pairs.keys():
                return False
            else:
                open_bracket = stack.pop()
                if pairs[open_bracket] == symb:
                    continue
                else:
                    return False
        return len(stack) == 0 
    

obj = Solution()
#s = input("Введите строку: ")
s = ")"
print(obj.isValid(s))