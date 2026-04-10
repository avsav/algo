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
        curr_sum += 1 if string[i] in "([{" else -1
        if min_sum > curr_sum:
            min_sum = curr_sum
            k = i
    
    if valid_parenthesis(string[k + 1:] + string[:k + 1]):
        return "YES"

    return "NO"


def main():
    #string = input()
    string1 = "}()[]{"
    print(string1, f(string1) == "YES")
    string2 = "}([)]{"
    print(string2, f(string2) == "NO")
    string3 = "()]["
    print(string3, f(string3) == "YES")
    string4 = "][]][{}]{()}[]{({})()}(){}{}[](){}{}{()}[][{}[]{}[{}]()][]{}()[][]()[]{}[]()()()([([])][])[]{}{}(()){}[]()()[(())][]()[]{{}}{}[][[]()()]{}{}(){[()]}[]{[]}[]()[]()[][](){[]}{}[]()()[][[]]({{}})[{}(){}["
    print(string4, f(string4) == "YES")
    string5 = "][]][{}(){}[" 
    print(string5, f(string5) == "YES")
    string6 = "()" 
    print(string6, f(string6) == "YES")
    

if __name__ == '__main__':
    main()