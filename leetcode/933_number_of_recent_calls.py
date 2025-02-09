# https://leetcode.com/problems/number-of-recent-calls/description/

class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        li = self.requests

        while li[0] < t - 3000:
            li.pop(0)
        return len(li)
        """
        n = len(li)
        for l in li:
            if l < t - 3000:
                n -= 1
            else:
                return n
        """        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
obj = RecentCounter()
param_1 = obj.ping(1)
param_2 = obj.ping(100)
param_3 = obj.ping(3001)
param_4 = obj.ping(3002)
print(param_1)
print(param_2)
print(param_3)
print(param_4)