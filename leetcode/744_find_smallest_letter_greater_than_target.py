def nextGreatestLetter(letters, target):
    low = 0
    high = len(letters) - 1
    ans = ""
    while (low <= high):
        mi = (low + high) // 2
        if (letters[mi] <= target):
            low = mi + 1
        else:
            ans = letters[mi]
            high = mi - 1
    if ans == "":
        return letters[0]
    return ans            

    #return letters[0]
        

letters = ["x","x","y","y"]
target = "z"
print(nextGreatestLetter(letters, target))
