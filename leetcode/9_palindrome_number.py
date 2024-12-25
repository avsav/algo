# https://leetcode.com/problems/palindrome-number/description/

def isPalindrome(x):
    n = x
    rev = rem = 0
    while(x > 0):
        rem = x % 10
        x //= 10
        rev = 10 * rev + rem
    if rev == n: return True
    return False


n = int(input())
print(isPalindrome(n))