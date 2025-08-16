# https://leetcode.com/problems/combination-sum/description

def combinationSum(candidates, target):
    n = len(candidates)
    res = []
    comb = []

    def backtrack(i, currSum):
        if currSum == target:
            res.append(comb[:])
            return
        
        if i == n or currSum > target:
            return

        currSum += candidates[i]
        comb.append(candidates[i])
        backtrack(i, currSum)
        comb.pop()
        backtrack(i + 1, currSum - candidates[i])
                
    backtrack(0, 0)

    return res



candidates1 = [2,3,6,7]
target1 = 7
candidates2 = [2,3,5]
target2 = 8
candidates3 = [2]
target3 = 1
print(combinationSum(candidates2, target2))