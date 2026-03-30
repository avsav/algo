import sys


def f(digits):
    cd = [0] * 10
    for d in digits:
        cd[int(d)] += 1

    rem = sum([i * cd[i] for i in range(10)]) % 3

    r1 = sorted([int(d) for d in digits if d in '147'])
    r2 = sorted([int(d) for d in digits if d in '258'])

    if rem == 1:
        if r1:
            cd[r1[0]] -= 1
        else:
            cd[r2[0]] -= 1
            cd[r2[1]] -= 1

    if rem == 2:
        if r2:
            cd[r2[0]] -= 1
        else:
            cd[r1[0]] -= 1
            cd[r1[1]] -= 1

    ans = ""
    for i in range(10):
        ans += (cd[9 - i]) * str(9 - i)
    
    return ans


def main():
    #digits = input()
    digits1 = "105"
    digits2 = "2222"
    digits3 = "000"
    digits4 = "54321"
    digits5 = "55553"
    digits6 = "990043964"
    digits7 = "4911815"
    digits8 = "969569692"
    print(f(digits8))


if __name__ == '__main__':
    main()