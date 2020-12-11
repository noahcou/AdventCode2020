# Day 1 code!
# Gotta do my taxes

f = open("Day1.txt", "r")
lst = f.readlines()
f.close()

def main1():
    for x in range(0, len(lst)):
        for y in range(x, len(lst)):
            a = int(lst[x])
            b = int(lst[y])
            if a + b == 2020:
                return a*b

def main2():
    for x in range(0, len(lst)):
        for y in range(x, len(lst)):
            for z in range(y, len(lst)):
                a = int(lst[x])
                b = int(lst[y])
                c = int(lst[z])
                if a + b + c == 2020:
                    return a*b*c

print(main1(), main2())