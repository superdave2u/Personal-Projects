#!/usr/bin/env python3

def series(x):
    SumList = []
    for n in range(0, x):
        SumList.append(((-1) ** n)/((2 * n + 3) ** 3 - (2 * n + 3)))
    return((4 * ((3/4) + sum(SumList))))


if __name__ == "__main__":
    Ans30 = 0
    AnsCount = 0
    count = 0

    while True:
        Series30 = "{0:.30f}".format(series(count))
        if Ans30 == Series30:
            AnsCount = AnsCount + 1
        else:
            Ans30 = Series30
            AnsCount = 0
        if AnsCount >= 1000:
            print("Winner winner chicken dinner!!! Pi = {}".format(Ans30))
            break
        count = count + 1
        print(count)
        print(Ans30)
