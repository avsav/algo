import sys
import time


def f(n, types):
    n = len(types)
    ans = 0
    d = {}
    l = 0
    for r in range(n):
        d[types[r]] = d.get(types[r], 0) + 1
        while len(d) > 2:
            d[types[l]] -= 1
            if d[types[l]] == 0:
                del d[types[l]]
            l += 1
        if len(d) == 2:
            ans = max(ans, r - l + 1)
    return ans


def main():   
    n1 = 10
    types1 = [1,2,2,1,1,4,4,4,4,4]
    print(n1, types1, f(n1, types1) == 7)
    n2 = 6
    types2 = [3,3,1,2,2,1]
    print(n2, types2, f(n2, types2) == 4)
    n3 = 2
    types3 = [1,1]  
    print(n3, types3, f(n3, types3) == 0)
    """
    with open("in_comp7_b_9.0_2026.txt") as fin:
        lines = fin.read().splitlines()
        n = int(lines[0])
        types = [int(i) - 1 for i in lines[1].split()]
    """
    """
    #n = int(input())
    #types = list(map(int, input().split()))
    t = time.perf_counter()
    print(f(n, types))
    print(f"Elapsed time: {time.perf_counter() - t}")
    """


if __name__ == '__main__':
    main()