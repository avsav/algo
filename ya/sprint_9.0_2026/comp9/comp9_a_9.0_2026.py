import sys


def f(string):
    n = len(string)
    scores = [ord(s) - ord("A") for s in string] 
    bad_score = max(scores)
    avg_score = sum(scores) / n
    avg_score = int(avg_score) + 1 if avg_score - int(avg_score) > .5 else int(avg_score)
    avg_score = bad_score - 1 if bad_score - avg_score > 1 else avg_score
    return chr(avg_score + ord("A")) 


def main():
    """
    string = input()
    print(f(string))
    """
    #"""
    string1 = "ABACABA"
    print(string1, f(string1) == "B")
    string2 = "AZAA"
    print(string2, f(string2) == "Y")    
    string3 = "ABABAB"
    print(string3, f(string3) == "A")
    string4 = "ABABBAABABABABB"
    print(string4, f(string4) == "B")
    #"""


if __name__ == '__main__':
    main()