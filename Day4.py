# Day 4
# Glory to North Pole

f = open("Day4.txt", "r")
lst = list()
for x in f.readlines():
        lst.append(x[:-1])

def main1():
    ans = 0
    tmp = list()
    
    for x in range(0, len(lst)):
        if len(lst[x]) < 3:
            if eval1(tmp):
                ans += 1
            tmp.clear()
        elif x == len(lst) - 1:
            tmp.append(lst[x])
            if eval1(tmp):
                ans += 1
            tmp.clear()
        else:
            tmp.append(lst[x])

    return ans

def main2():
    ans = 0

    tmp = list()
    
    for x in range(0, len(lst)):
        if len(lst[x]) < 3:
            if eval(tmp):
                ans += 1
            tmp.clear()
        elif x == len(lst) - 1:
            tmp.append(lst[x])
            if eval(tmp):
                ans += 1
            tmp.clear()
        else:
            tmp.append(lst[x])

    return ans

def eval(pp):
    val = 0
    dicty = {
        "byr" : False,
        "iyr" : False,
        "eyr" : False,
        "hgt" : False,
        "hcl" : False,
        "ecl" : False,
        "pid" : False,
    }
    for x in pp:
        for y in x.split(" "):
            yl = y.split(":")
            for z in range(0, len(yl)):
                if yl[z] in dicty:
                    dicty[yl[z]] = yl[z+1]
    for x in dicty:
        if x == "byr":
            try:
                if 1920 <= int(dicty[x]) <= 2002:
                    dicty[x] = True
            except: 
                dicty[x] = False
        if x == "iyr":
            try:
                if 2010 <= int(dicty[x]) <= 2020:
                    dicty[x] = True
            except: 
                dicty[x] = False
        if x == "eyr":
            try:
                if 2020 <= int(dicty[x]) <= 2030:
                    dicty[x] = True
            except: 
                dicty[x] = False
        if x == "hgt":
            try:
                if (dicty[x][:-2] == "in" and 59 <= int(dicty[x][:2]) <= 76) or (dicty[x][:-2] == "cm" and 150 <= int(dicty[x][:3]) <= 193):
                    dicty[x] = True
            except:
                dicty[x] = False
        if x == "hcl":
            for z in dicty[x]:
                if not(ord("0") <= ord(z) <= ord("9") or ord("a") <= ord(z) <= ord("f") or z == "#"):
                    dicty[x] = False
            if dicty[x] is not bool and len(dicty[x]) == 7:
                dicty[x] == True
        if x == "ecl":
            ecll = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            try:
                if dicty[x] in ecll:
                    dicty[x] = True
            except:
                dicty[x] = False
        if x == "pid":
            try:
                for z in dicty[x]:
                    if not(0 <= z <= 9):
                        dicty[x] = False
                if dicty[x] is not bool and len(dicty[x]) == 9:
                    dicty[x] = True
            except:
                dicty[x] = False

    for x in dicty:
        if dicty[x] == True:
            val += 1
    if val == 7:
        return True
                    


def eval1(pp, ccid = False):
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
        if dicty[x] == True:
            val += 1
    if val == 7 and not ccid and dicty["cid"] == False:
        return True
    elif val == 8:
        return True
    else:
        return False
    



print(main1(), main2())