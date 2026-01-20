def maxDistToClosest(seats):
    n = len(seats)
    i = 0
    max_dist = 1
    for j in range(1, n):
        if seats[i] == 0 and seats[j] == 1:
            max_dist = max(max_dist, j - i)
            i = j
        if seats[i] == 1 and seats[j] == 1:
            max_dist = max(max_dist, (j - i)//2)
            i = j
        if j == n - 1 and seats[j] == 0:
            max_dist = max(max_dist, n - 1 - i)
    return max_dist



seats1 = [1,0,0,0,1,0,1]
seats2 = [1,0,0,0]
seats3 = [0,1]
seats4 = [0,1,1]
seats5 = [0,0,0,0,0,1]
seats6 = [1,0,0,0,1,0,1,0,0,0,0,0,0]
print(maxDistToClosest(seats6))
