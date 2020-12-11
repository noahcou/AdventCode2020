# Day 3
# treeees

f = open("Day3.txt", "r")
lst = list()
for x in f.readlines():
    lst.append(x[:-1])
f.close()

def main1():
    ans = 0
    x = 3
    for y in range(1, len(lst)):
        if lst[y][x] == "#":
            ans += 1
        x += 3
        if x >= len(lst[y]):
            x -= len(lst[y])


    return ans

def main2():
    return tree(1)*tree(3)*tree(5)*tree(7)*tree(1, 2)

def tree(right, step = 1):
    ans = 0
    x = right
    for y in range(step, len(lst), step):
        if lst[y][x] == "#":
            ans += 1
        x += right
        if x >= len(lst[y]):
            x -= len(lst[y])


    return ans




print(main1(), main2())