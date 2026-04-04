import sys


def f(n, k, a):
    ans = 0
    min_sum = min(0, a[0])
    curr_sum = 0
    for i in range(n):
        curr_sum += a[i]
        if min_sum % k != curr_sum % k:
            ans = max(ans, curr_sum - min_sum)
        min_sum = min(min_sum, curr_sum)

    return ans


def main():
    #n, k = map(int, input().split())
    #a = list(map(int, input().split()))
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
    print(n6, k6, a6, f(n6, k6, a6) == 0)
    #print(f(n, k, a))


if __name__ == '__main__':
    main()