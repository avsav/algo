import sys


def ship_type(field, r, c):
    type = 0
    hor = False
    k = 1
    while field[r][c + k] != ".":
        hor = True
        if field[r - 1][c + k] != "." or field[r + 1][c + k] != ".":
            return -1       
        k += 1
    vert = False
    m = 1
    while field[r + m][c] != ".":
        vert = True
        if field[r + m][c - 1] != "." or field[r + m][c + 1] != ".":
            return -1       
        m += 1

    if hor:
        type = k
    
    if vert:
        type = m

    if not hor and not vert:
        type = 1

    if type > 4:
        type = -1

    return type


def f(field):
    corr_cnt = {1 : 4, 2 : 3, 3 : 2, 4 : 1}
    cnt = {1 : 0, 2 : 0, 3 : 0, 4 : 0}
    for r in range(1, 11):
        for c in range(1, 11):
            if field[r][c] == "#" and field[r][c - 1] == "." and field[r - 1][c] == ".":
                type = ship_type(field, r, c)
                if type == -1:
                    return "NO"
                cnt[type] += 1
    
    if cnt == corr_cnt:
        return "YES"
    
    return "NO"


def main():
    field = ["." + input() + "." for _ in range(10)]
    field.insert(0, "." * 12)
    field.append("." * 12)
    print(f(field))
    #print(ship_type(field, 7, 8))


if __name__ == '__main__':
    main()