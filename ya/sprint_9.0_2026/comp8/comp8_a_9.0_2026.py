import sys


def f(string):
    dir = {'U':(0,1),'R':(1,0),'D':(0,-1),'L':(-1,0)}
    d = {(0,0):1}
    curr_point = (0,0)
    for s in string:
        curr_point = tuple(map(sum, zip(curr_point, dir[s])))
        d[curr_point] = d.get(curr_point, 0) + 1
    ans = 0 
    for val in d.values():
        if val > 1:
            ans += 1
        
    return ans


def main():
    #string = input()
    string1 = "ULDRULDRULDRULDRULDRULDRULDRULDRULDRULDR"
    print(string1, f(string1) == 4)
    string2 = "ULDR"
    print(string2, f(string2) == 1)    
    string3 = "ULRD"
    print(string3, f(string3) == 2)


if __name__ == '__main__':
    main()