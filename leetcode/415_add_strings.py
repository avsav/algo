# https://leetcode.com/problems/add-strings/

def addStrings(num1, num2):
    #sys.set_int_max_str_digits(10000) 
    n1 = stringToInt(num1)
    n2 = stringToInt(num2)

    return n1 + n2
    
def stringToInt(string):
    num = 0
    for i in range(len(string)):
        num = num * 10 + ord(string[i]) - ord('0')
    return num

num1 = "11"
num2 = "123"
#print(ord("3") - ord("0"))
print(addStrings(num1, num2))