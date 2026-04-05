import sys


def f(n, k, a):
    min1 = 0
    min2 = 10**11
    max_sum = 0
    prefix = 0
    """
    prefix = [0]
    for i in range(n):
        prefix.append(prefix[-1] + a[i])
    """
    for i in range(n):
        prefix += a[i]
        if prefix - min1 > max_sum and (prefix - min1) % k:
            max_sum = prefix - min1
        if prefix - min2 > max_sum and (prefix - min2) % k:
            max_sum = prefix - min2
        if prefix < min1:
            if min1 % k == prefix % k:
                min1 = prefix
            else:
                min2 = min1
                min1 = prefix
        if prefix > min1 and prefix < min2 and prefix % k != min1 % k:
            min2 = prefix

    return max_sum


def main():
    """
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(f(n, k, a))
    """
    #"""
    n1, k1 = 3, 6
    a1 = [3,2,1]
    print(n1, k1, a1, f(n1, k1, a1) == 5)
    n2, k2 = 5, 15
    a2 = [5,2,4,1,3]
    print(n2, k2, a2, f(n2, k2, a2) == 12)
    n3, k3 = 5, 4
    a3 = [5,2,4,1,3]
    print(n3, k3, a3, f(n3, k3, a3) == 15)
    n4, k4 = 5, 2
    a4 = [-1,2,-1,2,-1]
    print(n4, k4, a4, f(n4, k4, a4) == 3)
    n5, k5 = 3, 2
    a5 = [-2,2,-4]
    print(n5, k5, a5, f(n5, k5, a5) == 0)
    n6, k6 = 20, 5
    a6 = [-58,61,183,-94,180,-75,-76,-76,-29,-72,-59,162,-16,-18,102,-42,-34,186,-45,70]
    print(n6, k6, a6, f(n6, k6, a6) == 308)
    n7, k7 = 10, 2
    a7 = [-4,-10,10,5,3,-3,0,-9,-7,-7]
    print(n7, k7, a7, f(n7, k7, a7) == 15)
    n8, k8 = 10, 5
    a8 = [11,83,90,-31,39,88,-94,-32,-89,-25]
    print(n8, k8, a8, f(n8, k8, a8) == 269)
    #"""


if __name__ == '__main__':
    main()