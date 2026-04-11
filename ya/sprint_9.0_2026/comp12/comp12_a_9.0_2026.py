import sys


def f(balls):
    n = int(balls[0])
    balls += "10"
    d = {}
    stack = []
    for i in range(1, n + 2):
        if stack and balls[i] != stack[-1] and d[stack[-1]] >= 3:
            last = stack[-1]
            while d[last] > 0:
                d[last] -= 1
                stack.pop()

        if i != n + 1:
            stack.append(balls[i])
            d[balls[i]] = d.get(balls[i], 0) + 1

    return n - len(stack)


def main():
    balls = list(input().split())
    print(f(balls))


if __name__ == '__main__':
    main()