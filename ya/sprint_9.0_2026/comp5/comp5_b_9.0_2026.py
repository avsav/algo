import sys


def f(string):
    max_cnt = max(string.count(s) for s in set(string))
    ans = 0
    for s in set(string):
        if string.count(s) != max_cnt:
            continue
        ind_max_cnt = [i for i in range(len(string)) if string[i] == s]
        
        k = 1
        while all(i + k < len(string) and string[i + k] == string[ind_max_cnt[0] + k] for i in ind_max_cnt):
            k += 1

        ans = max(ans, k)
 
    return ans


def main():
    #string = input()
    string1 = "abacaba"
    string2 = "abab"
    string3 = "aaabbb"
    print(f(string3))


if __name__ == '__main__':
    main()