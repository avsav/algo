def maxDistToClosest(seats):
    n = len(seats)
    i = 0
    max_dist = 1
    for j in range(1, n):
        if seats[i] == 1:
            max_dist = max(max_dist, j - i)
            i = j
        if seats[i] == 1 and seats[j] == 1:
            max_dist = max(max_dist, (j - i)//2)
            i = j
    return max_dist


seats = [1,0,0,0,1,0,1]
print(maxDistToClosest(seats))
