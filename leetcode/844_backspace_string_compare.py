# https://leetcode.com/problems/backspace-string-compare/description/

def backspaceCompare(s, t):
    
    def delete_backspace(string):
        n = len(string)
        stack = []
        for s in string:
            if s != '#':
                stack.append(s)
            elif stack:
                stack.pop()
        return stack
    
    s = delete_backspace(s)
    t = delete_backspace(t)

    return s == t


s = "a##c"
t = "#a#c"
print(backspaceCompare(s,t))