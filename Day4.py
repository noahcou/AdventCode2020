# Day 4
# Glory to North Pole

f = open("Day4.txt", "r")
lst = list()
for x in f.readlines():
    lst.append(x[:-1])
f.close()

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
                else:
                    dicty[x] = False
            except:
                print(f"byr except: {dicty[x]}")

        if x == "iyr":
            try:
                if 2010 <= int(dicty[x]) <= 2020:
                    dicty[x] = True
                else:
                    dicty[x] = False
            except: 
                print(f"iyr except: {dicty[x]}")

        if x == "eyr":
            try:
                if 2020 <= int(dicty[x]) <= 2030:
                    dicty[x] = True
                else:
                    dicty[x] = False
            except: 
                print(f"eyr except: {dicty[x]}")

        if x == "hgt":
            try:
                if str(dicty[x]).strip().endswith("cm"):
                    if 150 <= int(dicty[x][:3]) <= 193:
                        dicty[x] = True
                elif str(dicty[x]).strip().endswith("in"):
                    if 59 <= int(dicty[x][:2]) <= 76:
                        dicty[x] = True
                else:
                    dicty[x] = False
            except: 
                print(f"hgt except: {dicty[x]}")

        if x == "hcl":
            try:
                if dicty[x][0] == "#":
                    for y in dicty[x][1:]:
                        if not (ord('0') <= ord(y) <= ord('9') or ord('a') <= ord(y) <= ord('f')):
                            dicty[x] = False
                    if dicty[x] != False:
                        dicty[x] = True
                else:
                    dicty[x] = False
            except:
                print(f"hcl except: {dicty[x]}")

        if x == "ecl":
            ecll = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            try:
                if dicty[x] in ecll:
                    dicty[x] = True
                else:
                    dicty[x] = False
            except:
                print(f"ecl except: {dicty[x]}")

        if x == "pid":
            try: 
                if len(dicty[x]) == 9:
                    for y in dicty[x]:
                        if not (ord('0') <= ord(y) <= ord('9')):
                            dicty[x] = False
                    if dicty[x] != False:
                        dicty[x] = True
                else:
                    dicty[x] = False
            except:
                print(f"pid except: {dicty[x]}")

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