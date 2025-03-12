# https://leetcode.com/problems/string-compression/description/

def compress(chars):
    n = len(chars)
    right = 0
    spi = []
    res = 0
    while right < n:
        left = right
        cnt = 0
        res += 1
        spi.append(chars[left])
        while right < n and chars[left] == chars[right]:
            right += 1
            cnt += 1
    if cnt > 10:
        lcnt = [_ for _ in str(cnt)]
        spi.extend(lcnt)
        res += len(str(cnt))
    return spi



chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(compress(chars))