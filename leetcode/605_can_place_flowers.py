# https://leetcode.com/problems/can-place-flowers/description/

def canPlaceFlowers(flowerbed, n):
    # Stupid solution
    if n == 0:
        return True
    k = len(flowerbed)
    if k == 1 and flowerbed[0] == 0:
        return True
    if k >= 2 and flowerbed[0] == 0 and flowerbed[1] == 0:
        n -= 1
        flowerbed[0] = 1
    if n == 0:
        return True
    if k >= 2 and flowerbed[k - 1] == 0 and flowerbed[k - 2] == 0:
        n -= 1
        flowerbed[k - 1] = 1
    if n == 0:
        return True
    for i in range(1, k - 1):
        if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
            n -= 1
            flowerbed[i] = 1
        if n == 0:
            return True

    return False


flowerbed1 = [1,0,0,0,1]
n1 = 1
flowerbed2 = [1,0,0,0,1]
n2 = 2
flowerbed3 = [0,1,0,1,0]
n3 = 1
flowerbed4 = [1,0,0,0,0,1]
n4 = 2
flowerbed5 = [0,0,1,0,1]
n5 = 1
flowerbed6 = [0,0,0,0,1]
n6 = 2

print(canPlaceFlowers(flowerbed6, n6))