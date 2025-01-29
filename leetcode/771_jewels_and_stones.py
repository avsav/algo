# https://leetcode.com/problems/jewels-and-stones/

def numJewelsInStones(jewel, stones):
    #lj = [x for x in jewel]
    cnt = 0
    for s in stones:
        if s in jewels:
            cnt += 1
    return cnt


jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))
