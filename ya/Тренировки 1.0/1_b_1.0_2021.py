def f(a, b, c): 
    if a + b + c > 2 * max(a, b, c):
        return "YES"
    return "NO"


a = int(input())
b = int(input())
c = int(input())
print(f(a, b, c))