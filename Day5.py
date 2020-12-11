# Day 5
# weird boarding passes

f = open("Day5.txt", "r")
lst = list()
for x in f.readlines():
    lst.append(x[:-1])
f.close()

def main():
    ans = 0
    ans2 = 0
    tmp = list()

    for x in lst:
        rows = [x for x in range(128)]
        columns = [x for x in range(8)]
        for y in x:
            if y == "F":
                rows = rows[:int(len(rows)/2)]
            if y == "B":
                rows = rows[int(len(rows)/2):]
            if y == "L":
                columns = columns[:int(len(columns)/2)]
            if y == "R":
                columns = columns[int(len(columns)/2):]
            
        tmp.append((rows[0] * 8) + columns[0])
    
    tmp.sort()

    for x in range(len(tmp) - 1):
        if tmp[x] + 1 != tmp[x+1]:
            ans2 = tmp[x] + 1
    
    ans = tmp[-1]
    return f"{ans} {ans2}"

print(main())