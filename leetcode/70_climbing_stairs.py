# https://leetcode.com/problems/climbing-stairs/description/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # by @idfumg
        def rec(steps):
            if steps > n: return 0
            if steps == n: return 1
            #print(f"rec({steps} + 1) + rec({steps} + 2)")
            #print(rec(steps + 1) + rec(steps + 2))
            return rec(steps + 1) + rec(steps + 2)
        
        return rec(0)

sol = Solution()
n = int(input())
print(sol.climbStairs(n))