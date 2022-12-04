def get_input():
    with open("input.txt") as f:
        return [int(i) for i in f.read().replace(",","\n").replace("-","\n").split("\n")[:-1]]

inp = get_input()
count = 0
for i in range(3,len(inp),4):
    count+=1 if (inp[i-3] <= inp[i-1] and inp[i-2] >= inp[i]) or (inp[i-1] <= inp[i-3] and inp[i] >= inp[i-2]) else 0
print("Part 1 " + str(count))
count = 0
for i in range(3,len(inp),4):
    count+=1 if (inp[i-1] >= inp[i-3] and inp[i-1] <= inp[i-2]) or (inp[i-3] >= inp[i-1] and inp[i-3] <= inp[i]) else 0
print("Part 2 " + str(count))
                                                            
    

