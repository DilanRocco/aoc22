with open("input.txt") as f:
    key = f.read()
    def find_non_dup(length):
        vals = {}
        for i in range(len(key)):
            if key[i] not in vals:
                vals[key[i]] = 0
            vals[key[i]] +=1    
            if sum(v for v in vals.values()) <= length: continue
            vals[key[i-length]] -= 1
            if any(vals[map_key] > 1 for map_key in vals):
                continue
            return i+1

print("Part One: " + str(find_non_dup(4)))
print("Part Two: " + str(find_non_dup(14)))




