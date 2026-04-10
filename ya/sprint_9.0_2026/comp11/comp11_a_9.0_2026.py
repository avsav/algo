import sys


def valid_parenthesis(string):
    parenthesis = ["()", "[]", "{}"]
    stack = []
    for s in string:
        if stack and stack[-1] + s in parenthesis:
            stack.pop()
        else: 
            stack.append(s)
    
    return not stack


def f(string):
    n = len(string)
    k = 0
    min_sum = curr_sum = 0
    for i in range(n):
        curr_sum += 0 if string[i] in "([{" else -1
        if min_sum > curr_sum:
            min_sum = curr_sum
            k = i
    
    if valid_parenthesis(string[k + 1:] + string[:k + 1]):
        return "YES"

    return "NO"


def main():
    #string = input()
    string1 = "}()[]{"
    string2 = "}([)]{"
    string3 = "()]["
    string4 = "][]][{}]{()}[]{({})()}(){}{}[](){}{}{()}[][{}[]{}[{}]()][]{}()[][]()[]{}[]()()()([([])][])[]{}{}(()){}[]()()[(())][]()[]{{}}{}[][[]()()]{}{}(){[()]}[]{[]}[]()[]()[][](){[]}{}[]()()[][[]]({{}})[{}(){}["
    print(f(string4))


if __name__ == '__main__':
    main()