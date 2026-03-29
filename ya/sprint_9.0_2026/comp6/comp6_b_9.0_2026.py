import sys
import time


def f(n, a):
    guests = set(i for i in range(n))
    shift = 0
    shifts = set()
    #shifts = [0] * n
    for i in range(n):
        k = a.index(i)
        if k >= i:
            shift = (n - k + i) % n
        else:
            shift = i - k
        shifts.add(shift)
        #shifts[i] = shift

        
    """
    for j in range(n):
        for i in range(n):
            if a[i - j] == i + 1:
                ans += 1
                break
            if i == n - 1 and a[i - j] != i + 1:
                return ans
    """
    """
    for j in range(n):
        if all(a[i - j] != i + 1 for i in range(n)):
            return ans
        else:
            ans += 1
    """
    """
    for i in range(n):
        if all(a[i] != i + 1 for i in range(n)):
            return ans
        else:
            ans += 1
        last = a.pop()
        a.insert(0, last)
    """
    if len(shifts) == n:
        return -1
    
    ans = min(guests - shifts)
    
    return ans


def main():
    #n = int(input())
    #a = [int(i) - 1 for i in input().split()]
    with open("in2_comp6_b_9.0_2026.txt") as fin:
        lines = fin.read().splitlines()
        n = int(lines[0])
        a = [int(i) - 1 for i in lines[1].split()]
    t = time.perf_counter()
    print(f(n, a))
    print(f"Elapsed time: {time.perf_counter() - t}")

    #print(a)


if __name__ == '__main__':
    main()