# https://leetcode.com/problems/maximum-binary-string-after-change/description


def maximumBinaryString(binary):
    n = len(binary)
    m = binary.count("1", binary.find("0"))

    k = binary.count("0")
    if k == 0:
        return binary

    res = "1"*(n - m - 1) + "0" + "1"*m
            
    return res





binary1 = "000110"
binary2 = "01"
binary3 = "1100"
print(maximumBinaryString(binary1))