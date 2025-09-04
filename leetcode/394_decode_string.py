# https://leetcode.com/problems/decode-string/description/?envType=problem-list-v2&envId=nb4ro6ft

def decodeString(s):
    n = len(s)
    currStr = ""
    stack = []
    currNum = 0
    for i in range(n):
        if s[i].isdigit():
            currNum = 10 * currNum + int(s[i])
        elif s[i] == "[":
            stack.append(currNum)
            stack.append(currStr)
            currNum = 0
            currStr = ""
        elif s[i] == "]":
            prevStr = stack.pop()
            prevNum = stack.pop() 
            currStr = prevStr + prevNum * currStr
        else:
            currStr += s[i]

    return currStr



s0 = "3[a]"
s1 = "3[a]2[bc]"
s2 = "3[a2[c]]"
s3 = "3[a2[c]]"
print(decodeString(s1))