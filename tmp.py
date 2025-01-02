import time


# fib
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n - 1) + fib(n - 2)

# memoization fib
def mfib(n):
    arr = []
    arr.append(0)
    arr.append(1)
    for i in range(2, n + 1):
        arr.append(arr[i - 1] + arr[i - 2])
    return arr[n]

'''
n = 40

t1 = time.perf_counter()
ans1 = fib(n)
print(f"Fib elapsed time: {time.perf_counter() - t1}")
print(ans1)


print

t2 = time.perf_counter()
ans2 = mfib(n)
print(f"Memo fib elapsed time: {time.perf_counter() - t2}")
print(ans2)


#print(mfib(n))
'''

#d = {node: dict() for node in range(5)} 
#print(d)

di = {0: {1: 5, 2: 3},
      1: {3: 1, 4: 15},
      2: {5: 7, 8: 9},
      3: {6: 4, 7: 8}
     }

