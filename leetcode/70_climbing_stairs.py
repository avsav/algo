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
        
        # my dp solution
        def dpf(n):
            dp = [0] * (n + 1)
            dp[0] = dp[1] = 1
            for i in range(2, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]
            return dp[n]
        
        # optimal dp solution
        def odpf(n):
            prev = next = 1
            for i in range(2, n + 1):
                prev = next
                next = prev + next
            return next        
        
        return odpf(n)
    

     
sol = Solution()
n = int(input())
print(sol.climbStairs(n))