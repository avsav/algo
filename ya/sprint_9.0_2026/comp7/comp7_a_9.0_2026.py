import sys


def f(n, string):
    nums = [1 if s == 'a' else -1 for s in string]
    n = len(nums)
    prefix = 0
    d = {0: 1}
    ans = 0
    for i in range(n):
        prefix += nums[i]
        ans += d.get(prefix, 0)
        d[prefix] = d.get(prefix, 0) + 1
        
    return ans


def main():
    n = int(input())
    string = input()
    print(f(n, string))


if __name__ == '__main__':
    main()