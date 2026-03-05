def f(a, b, c, d, e): 
    if min(d, e) >= min(a, b, c) and max(d, e) >= a + b + c - min(a, b, c) - max(a, b, c):
        return "YES"
    return "NO"


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print(f(a, b, c, d, e))