# https://leetcode.com/problems/path-crossing/description/

def isPathCrossing(path):
    hm = {"N":(0,1), 
          "S":(0,-1),
          "E":(1,0), 
          "W":(-1,0)}
    n = len(path)
    m = set()
    summ = (0,0)
    for i in range(n):
        m.add(summ)
        tmp = []
        for j in range(2):
            tmp.append(summ[j] + hm[path[i]][j])
        tmp = tuple(tmp)
        summ = tmp
        if summ in m:
            return True

    return False
 
path1 = "NESWW"
path2 = "NES"
print(isPathCrossing(path2))