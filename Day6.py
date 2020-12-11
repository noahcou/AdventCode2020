# Day 6
# questionaires

f = open("Day6.txt", "r")
lst = list()
for x in f.readlines():
    lst.append(x[:-1])
f.close()

def main1():
    ans = 0
    tmp = list()

    for x in lst:
        if len(x) < 1:
            tmp.clear()
        else:
            for y in x:
                if y not in tmp:
                    ans += 1
                    tmp.append(y)

    return ans

def main2():
    ans = 0
    num = 0
    dicty = dict()

    for x in lst:
        if len(x) < 1:
            for y in dicty:
                if dicty[y] == num:
                    ans += 1
            num = 0
            dicty.clear()
        else:
            num += 1
            for y in x:
                if y not in dicty:
                    dicty[y] = 1
                else:
                    dicty[y] += 1

    return ans


print(main1(), main2())