import sys


def f(balls):
    n = int(balls[0])
    del_ball = None
    stack = []
    for i in range(1, n + 1):
        if len(stack) >= 2 and stack[-2] == stack[-1] and stack[-1] == balls[i]:
            stack.pop()
            stack.pop()
            del_ball = balls[i]

        if balls[i] != del_ball:
            del_ball = None
            stack.append(balls[i])

    return n - len(stack)


def main():
    #balls = list(input().split())
    #print(f(balls))
    balls1 = [5,1,3,3,3,2]
    print(balls1, f(balls1) == 3)
    balls2 = [10,3,3,2,1,1,1,2,2,3,3]
    print(balls2, f(balls2) == 10)
    balls3 = [3,0,0,0]
    print(balls3, f(balls3) == 3)
    balls4 = [10,9,9,2,2,9,9,9,9,2,2]
    print(balls4, f(balls4) == 8)
    balls5 = [31,1,0,0,2,2,3,3,4,4,5,5,6,6,7,7,8,8,8,8,7,6,6,5,5,4,3,3,0,0,1,1]
    print(balls5, f(balls5) == 22)
    balls6 = [100,4,4,3,4,3,3,4,3,4,4,5,4,3,3,4,4,3,3,4,3,3,4,4,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,3,3,4,4,5,4,3,3]
    print(balls6, f(balls6) == 67)
    balls7 = [15,4,4,3,4,3,3,4,3,4,4,5,4,4,4,4,5,3,3,4,4,5,4,3,3]
    print(balls7, f(balls7) == 4)


if __name__ == '__main__':
    main()