# Day 4
# Glory to North Pole

f = open("Day4.txt", "r")
w = open("Day4r.txt", "w")
lst = list()
for x in f.readlines():
        lst.append(x[:-1])

def main1():
    ans = 0
    tmp = list()
    
    for x in range(0, len(lst)):
        if len(lst[x]) < 3 or x == len(lst) - 1:
            w.write(f"{tmp}\n")
            if eval(tmp):
                ans += 1
                w.write(f"{ans}\n\n")
            tmp.clear()
        else:
            tmp.append(lst[x])

    return ans

def main2():
    ans = 0

    return ans

def eval(pp, ccid = False):
    val = 0
    dicty = {
        "byr" : False,
        "iyr" : False,
        "eyr" : False,
        "hgt" : False,
        "hcl" : False,
        "ecl" : False,
        "pid" : False,
        "cid" : False
    }

    for x in pp:
        for y in x.split(":"):
            if y[-3:] in dicty:
                dicty[y[-3:]] = True
    for x in dicty:
        w.write(f"{x} {dicty[x]}\n")
        if dicty[x] == True:
            val += 1
    if val == 7 and not ccid and dicty["cid"] == False:
        w.write("Tc\n")
        return True
    elif val == 8:
        w.write("T\n")
        return True
    else:
        w.write("F\n\n")
        return False
    



print(main1(), main2())
w.close()