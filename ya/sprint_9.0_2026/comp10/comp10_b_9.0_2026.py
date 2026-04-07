import sys


def f(n, m, k, cmds):
    buffer = []
    windows = [[] for _ in range(n)]
    win_num = 0
    for c in cmds:
        if c == "Next":
            win_num = (win_num + 1) % n
        elif c == "Paste":
            windows[win_num].extend(buffer) #or windows[win_num] += buffer
        elif c == "Copy":
            buffer = windows[win_num][-k:]
        elif c == "Backspace":
            if windows[win_num]:
                windows[win_num].pop()
        else:
            windows[win_num].append(c)
        
    if not windows[win_num]:
        return "Empty"

    return "".join(windows[win_num][-k:])


def main():
    n, m, k = map(int, input().split())
    cmds = [input() for _ in range(m)]
    print(f(n, m, k, cmds))


if __name__ == '__main__':
    main()