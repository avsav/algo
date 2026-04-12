import sys


def del_head(field):
    new_field = [list(f) for f in field]
    cnt = 0
    for r in range(1, 11):
        for c in range(1, 11):
            if field[r][c] == "#":
                if field[r - 1][c - 1] == "." and field[r][c - 1] == "." and field[r - 1][c] == ".":
                    new_field[r][c] = "."
                    cnt += 1
    
    new_field = ["".join(nf) for nf in new_field]

    return new_field, cnt


def f(field):
    field10, cnt10 = del_head(field)
    field6, cnt6 = del_head(field10)
    field3, cnt3 = del_head(field6)
    field1, cnt1 = del_head(field3)

    if cnt10 == 10 and cnt6 == 6 and cnt3 == 3 and cnt1 == 1:
        return "YES"
    
    return "NO"


def main():
    field = ["." + input() + "." for _ in range(10)]
    field.insert(0, "." * 12)
    field.append("." * 12)
    print(f(field))


if __name__ == '__main__':
    main()