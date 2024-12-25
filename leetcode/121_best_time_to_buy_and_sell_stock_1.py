# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

def maxProfit(prices):
    return sol3(prices)

# my first stupid solution
def sol1(prices):
    n = len(prices)
    max_list = []
    for i in range(n):
        max = 0
        for j in range(n - 1 - i):
            diff = prices[n - 1 - i] - prices[j]
            if diff > max: max = diff
        max_list.append(max)
    max = 0
    for i in max_list:
        if i > max: max = i
    return max

# my second not stupid solution
def sol2(prices):
    n = len(prices)
    buy = sell = 0
    profit = 0
    for i in range(n - 1):
        sell += 1
        while (prices[buy] > prices[sell]): 
            buy += 1
        profit = max(profit, prices[sell] - prices[buy])
    if profit < 0: return 0
    return profit

# my third not stupid solution (best version of solution 2)
def sol3(prices):
    n = len(prices)
    buy_price = prices[0]
    profit = 0
    for sell_price in prices:
        if (buy_price > sell_price): 
            buy_price = sell_price
        profit = max(profit, sell_price - buy_price)
    if profit < 0: return 0
    return profit

# recursion solution by @idfumg
def sol4(prices):
    n = len(prices)
    INF = 10**10
  
    def rec(i, taken):
        if i == n and taken: return -INF
        if i == n and not taken: return 0
        if taken: return max(prices[i], rec(i + 1, 1))
        return max(-prices[i] + rec(i + 1, 1), rec(i + 1, 0))
    
    return rec(0, 0)



prices = [2,1,2,1,0,1,2]
print(maxProfit(prices))