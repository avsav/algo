# https://leetcode.com/problems/string-compression/description/

def compress(chars):
    n = len(chars)
    right = 0
    k = 0
    while right < n:
        left = right
        cnt = 0
        chars[k] = chars[right] 
        while right < n and chars[left] == chars[right]:
            right += 1
            cnt += 1
        scnt = str(cnt)

        left = k
        if cnt > 1:
            for i in range(left + 1, left + len(scnt) + 1):
                chars[i] = scnt[i - left - 1]
            k = left + len(scnt) + 1
        else:
            k = left + 1       

    return len(chars[:k])


chars1 = ["a","a","a"]
chars2 = ["a","a","a","a","b","b","b","b","b","b","b","b","b","b","b","b"]
chars3 = ["a"]
chars4 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(compress(chars4))