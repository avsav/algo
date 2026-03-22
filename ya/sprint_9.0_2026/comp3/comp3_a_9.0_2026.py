import sys


def f(string):
    ans = ""
    string = list(string.split())
    for word in string:
        i = 0
        j = len(word) - 1
        while word[i] == chr(39):
            i += 1
        while word[j] == chr(39):
            j -= 1
        i = 2*i
        j = 2*j - len(word) + 2
        ans += word[i : j]

    return ans


def main():
    #string = input()
    string1 = "yandex'''' 'algo''' trainings''''" #output yatrain
    string2 = "'''abc"                            #output 
    string3 = "'''abcdef''"                       #output d
    string4 = "aa bb"                             #output aabb
    string5 = "aa d' 'h bb"                       #output aabb
    print(f(string2))


if __name__ == '__main__':
    main()