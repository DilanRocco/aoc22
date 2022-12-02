def input():
    with open("input.txt") as f:
        return f.read().replace("\n"," ").split(" ")
game = input()
#part one
total = 0
for i in range(1,len(game),2):
    me = ord(game[i]) - 23 - 64
    elf = ord(game[i-1]) - 64
    total += me 
    total += 3 if me == elf else 0    
    total += 6 if (me == 1 and elf == 3) or (me - elf == 1) else 0 
print("part one")
print(total)

#part two
total = 0
for i in range(1,len(game),2):
    me = ord(game[i]) - 23 - 64
    elf = ord(game[i-1]) - 64
    total += (me-1) * 3
    total += elf if me == 2 else 0    
    total += elf -1 if me == 1 and elf-1 != 0 else 3 if me == 1 else 0
    total += elf +1 if me == 3 and elf+1 != 4 else 1 if me == 3 else 0

print("part two")
print(total)


