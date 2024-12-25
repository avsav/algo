# https://leetcode.com/problems/counting-bits/description/

def countBits(n):

    def sum_digits(m):
        x = m
        #res = 0
        cnt = 0
        #k = 1
        while(x > 0):
            rem = x % 2   # x & 1
            cnt += rem
            x //= 2 
            #res = res + k * rem
            #k *= 10
        return cnt
    
    li =[]
    for i in range(n + 1):
        li.append(sum_digits(i))

    return li
    
    
n = 5
print(countBits(n))