def get_input():
    with open("input.txt") as f:
        return f.read().split("\n")[:-1]

def convert_chars_to_prior_num(dups):
    total = 0
    for char in dups:
        total += ord(char) - 96 if char.islower() else ord(char) - 38
    return total

rucks = get_input()
dups = []
for i in rucks:
    seen = {}
    half = len(i)//2
    l,r = i[:half], i[half:]
    for l_val in l: seen[l_val] = True
    for r_val in r:
        if r_val in seen:
            dups.append(r_val)
            break
print("Part One " + str(convert_chars_to_prior_num(dups)))

dups = []
for i in range(2,len(rucks),3):
    seen1 = {}
    seen2 = {}
    seen3 = {}
    for j in range(len(rucks[i])):seen1[rucks[i][j]] = True
    for k in range(len(rucks[i-1])): seen2[rucks[i-1][k]] = True
    for l in range(len(rucks[i-2])): seen3[rucks[i-2][l]] = True
    common = seen1.keys() & seen2.keys() & seen3.keys()
    dups.append(list(common)[0])
print("Part Two " + str(convert_chars_to_prior_num(dups)))





            







        



