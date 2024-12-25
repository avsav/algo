# https://leetcode.com/problems/climbing-stairs/description/

class Solution(object):
    def climbStairs(self, n):

        # by @idfumg
        def rec(steps):
            if steps > n: return 0
            if steps == n: return 1
            #print(f"rec({steps} + 1) + rec({steps} + 2)")
            #print(rec(steps + 1) + rec(steps + 2))
            return rec(steps + 1) + rec(steps + 2)
        
        # my stupid solution
        def f(n):
            if n == 0: return 1
            if n == 1: return 1
            return f(n - 1) + f(n - 2)
        
        # my memo solution
        def mf(n):
            arr = []
            arr.append(1)
            arr.append(1)
            for i in range(2, n + 1):
                arr.append(arr[i - 1] + arr[i - 2])
            return arr[n]
        
        return mf(n)
    

     
sol = Solution()
n = int(input())
print(sol.climbStairs(n))