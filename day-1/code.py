with open("input.txt") as f:
    t = f.read().split("\n")

all_cals,reindeer_cals = [], 0
for x in t: 
    if (x == ''):
        all_cals.append(reindeer_cals)
        reindeer_cals = 0
        continue
    reindeer_cals += int(x)

all_cals.sort(reverse=True)

print("Part One")
print(all_cals[0])
print("")

print("Part Two")
print(all_cals[0] + all_cals[1] + all_cals[2])

