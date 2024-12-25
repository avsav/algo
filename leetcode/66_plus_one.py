# https://leetcode.com/problems/plus-one/description/

def plusOne(digits):
    n = len(digits)
    k = 0
    for d in digits:
        k = 10 * k + d
    k += 1
    li =[]
    s = str(k)
    for i in range(len(s)):
        li.append(int(s[i]))
    return li

digits = [1, 9, 9]
print(plusOne(digits))

