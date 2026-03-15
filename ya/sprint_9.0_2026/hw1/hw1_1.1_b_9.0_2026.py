import sys
import math


def set_of_floors(m, k2, p2, n2):
    a = max(math.ceil(k2 / (n2 + m*(p2 - 1))), math.ceil(k2 / (m*p2))) 
    if p2 != 1 and n2 == 1:
        b = k2 / (m*(p2 - 1))
    if p2 == 1 and n2 != 1:
        b = k2 / (n2 - 1)
    if p2 != 1 and n2 != 1:
        b = min(k2 / (m*(p2 - 1)), k2 / (n2 - 1))
    k_set = set()
    k = a
    while k >= a and k < b:
        k_set.add(k)
        k += 1
    return k_set


def f(k1, m, k2, p2, n2):
    if p2 == 1 and n2 == 1:
        if k1 <= k2:
            print("1 1")
            return
        if m == 1:
            print("0 1")
            return
        if k1 <= k2*m:
            print("1 0")
            return
        print("0 0")
        return
    
    k_set = set_of_floors(m, k2, p2, n2)
    if n2 > m or not k_set:
        print("-1 -1")
        return

    p1_set = set()
    n1_set = set()
    for k in k_set:
        if k1 <= k*m:
            p1 = 1
            n1 = math.ceil(k1 / k)
        if k1 > k*m:
            p1 = math.ceil(k1 / (k*m))
            n1 = math.ceil((k1 - k*m*(p1 - 1)) / k)
        p1_set.add(p1)
        n1_set.add(n1)

    if len(p1_set) > 1 and len(n1_set) > 1:
        print("0 0")
        return
    if len(p1_set) > 1 and len(n1_set) == 1:
        print(f"0 {n1}")
        return  
    if len(p1_set) == 1 and len(n1_set) > 1:
        print(f"{p1} 0")
        return  

    print(f"{p1} {n1}")
    return 


def main():
    #k1, m, k2, p2, n2 = map(int, input().split())
    k11, m1, k21, p21, n21 = 89, 20, 41, 1, 11       #output 2 3
    k12, m2, k22, p22, n22 = 11, 1, 1, 1, 1          #output 0 1
    k13, m3, k23, p23, n23 = 3, 2, 2, 2, 1           #output -1 -1
    k14, m4, k24, p24, n24 = 118, 9, 115, 4, 2       #output 4 3
    k15, m5, k25, p25, n25 = 11, 2, 4, 1, 2          #output 0 2
    k16, m6, k26, p26, n26 = 5, 20, 2, 1, 1          #output 1 0
    k17, m7, k27, p27, n27 = 25, 3, 1, 1, 1          #output 0 0
    k18, m8, k28, p28, n28 = 1, 3, 1, 3, 1           #output -1 -1
    k19, m9, k29, p29, n29 = 1, 3, 1, 1, 3           #output -1 -1
    k10, m10, k210, p210, n210 = 1, 1, 42, 1, 1      #output 1 1
    k111, m11, k211, p211, n211 = 1, 2, 42, 1, 5      #output -1 -1
    k12, m12, k212, p212, n212 = 501, 20, 500, 1, 1  #output 1 0
    k13, m13, k213, p213, n213 = 5, 1000, 5, 1, 2    #output 1 2
    f(k111, m11, k211, p211, n211)
 

if __name__ == '__main__':
    main()