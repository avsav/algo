# https://leetcode.com/problems/daily-temperatures/description/?envType=problem-list-v2&envId=nb4ro6ft

def dailyTemperatures(temperatures):
    n = len(temperatures)
    stack = []
    res = [0] * n
    for i in range(n):  
        while stack and temperatures[i] > temperatures[stack[-1]]:
            last = stack.pop()
            res[last] = i - last
        stack.append(i)  

    return res




temperatures1 = [73,74,75,71,69,72,76,73]
temperatures2 = [30,40,50,60]
temperatures3 = [30,60,90]
temperatures4 = [4,3,2,1]
temperatures5 = [1,2,3,4]
print(dailyTemperatures(temperatures1))