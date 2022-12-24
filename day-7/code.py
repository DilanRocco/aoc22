import sys
def read_input():
    with open("input.txt") as f:
        return f.readlines()

#string of commands
command_lines = read_input()

directorys_inside = []
directorys_done = []


for line in command_lines:
    commands = line.split()
    if (len(commands) > 2 and commands[2] == ".."):
        directorys_done.append(directorys_inside.pop())
        continue
        
    if (len(commands) > 1 and commands[1] == "cd"):
        directorys_inside.append(0)
        continue
    if (commands[0].isnumeric()):
        for i in range(len(directorys_inside)):
            directorys_inside[i] += int(commands[0])

if (len(directorys_inside) > 0):
    for directory in directorys_inside:
        directorys_done.append(directory)

result = 0
for directory in directorys_done:
    print(directory)
    if directory <= 100000:
        result += directory



print("Part 1: " + str(result))



open_space_needed = 30000000 -(70000000 - max(directorys_done))
print(open_space_needed)
min_directory = sys.maxsize
for size in directorys_done:
    if (open_space_needed < size and min_directory > size):
        min_directory = size
print("Part 2: " + str(min_directory))






    





