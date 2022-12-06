from collections import deque
def get_input():
    with open("input.txt") as f:
        return f.readlines()

def get_stacks(lines):
    stacks = []
    for i in range(9):
        stack = []
        for j in range(8):
            ind = (i*4)+1
            val = lines[j][ind]
            if val != " ": stack.append(val) 
        stack.reverse()
        stacks.append(stack)
    return stacks


def get_moves(lines):
    moves = []
    for i in range(10,len(lines),1):
        [moves.append(int(j)) for j in lines[i].replace("move ","").replace("from ","").replace("to ","").split(" ")]
    return moves

def get_answer(stacks):
    ans = ""
    for i in range(len(stacks)):
        ans += stacks[i].pop()
    return ans;
     
lines = get_input()
stacks = get_stacks(lines)
moves = get_moves(lines)
for i in range(2,len(moves), 3):
    apply_num = moves[i-2]
    from_slot = moves[i-1]-1
    to_slot = moves[i]-1
    for i in range(apply_num):
        popped = stacks[from_slot].pop()
        stacks[to_slot].append(popped)

print("Part 1: " +get_answer(stacks))

stacks = get_stacks(lines)
for i in range(2,len(moves), 3):
    apply_num = moves[i-2]
    from_slot = moves[i-1]-1
    to_slot = moves[i]-1
    d = []
    for i in range(apply_num):
        d.append(stacks[from_slot].pop())
    while d: stacks[to_slot].append(d.pop())

print("Part 2: " + get_answer(stacks))


