def f(s): 
    n = len(s)
    res = []
    k = i = 0 
    while i < n:
        if i + 2 < n and s[i + 2] == "#":
            k = 10 * int(s[i]) + int(s[i + 1])
            i += 3
        else:
            k = int(s[i])
            i += 1
        res.append(chr(ord('a') + k - 1))
    
    return ''.join(res)


#s = int(input())
s1 = "8512#12#15#23#15#18#12#4"
s2 = "852"
s3 = "1212#"
print(f(s3))