def f(n, a): 
    if n == 1:
        print(1)
        return
    capital = a[0]
    k = 0
    for i in range(1, n):
        if a[i - 1] < a[i] and k == 0:
            k = i
        if k != 0:
            if a[i] >= capital:
                k = i
        capital += a[i]

    #print(k, "\n")

    for j in range(n):
        if k == 0:
            print(0)
        if k > 0 and j < k:
            print(0)
        elif k > 0 and j >= k:
            print(1)


#n = int(input())
#a = [int(i) for i in input().split()]
n1 = 4
a1 = [1,1,3,4]
n2 = 1
a2 = [3]
n3 = 6
a3 = [1,1,3,4,4,4]
n4 = 3
a4 = [4,4,4]
n5 = 7
a5 = [1,1,3,4,4,4,5]
n6 = 5
a6 = [5,10,15,25,30]
n7 = 6
a7 = [5,10,15,25,70,80]
f(n7, a7)