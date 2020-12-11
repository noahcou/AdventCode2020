# Day 2
# I'm a security analyst fixer man now

f = open("Day2.txt", "r")
lst = f.readlines()
f.close()

def main1():
    ans = 0
    for x in lst:
        arr = x.split(" ")
        low, high = int(arr[0].split("-")[0]), int(arr[0].split("-")[1])
        char = arr[1][0]
        passwd = arr[2]

        count = 0
        for y in passwd:
            if y == char:
                count += 1
        
        if low <= count <= high:
            ans += 1
    return ans

def main2():
    ans = 0
    for x in lst:
        arr = x.split(" ")
        fst, scnd = int(arr[0].split("-")[0]) - 1, int(arr[0].split("-")[1]) - 1
        char = arr[1][0]
        passwd = arr[2]

        if bool(passwd[fst] == char) != bool(passwd[scnd] == char):
            ans += 1
    return ans

print(main1(), main2())
