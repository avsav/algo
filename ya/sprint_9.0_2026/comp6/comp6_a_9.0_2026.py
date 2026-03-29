import sys


def f(string):
    ans = "".join(sorted(string, reverse=True))

    return ans


def main():
    string = input()
    print(f(string))


if __name__ == '__main__':
    main()