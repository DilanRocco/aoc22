all_cals,reindeer_cals = [], 0
with open("input.txt") as f:
    t = f.read().split("\n")
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
print(sum(all_cals[:3]))

