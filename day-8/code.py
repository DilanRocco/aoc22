def get_input():
    with open("input.txt") as f:
        return f.readlines()
list_of_trees = get_input()
len_of_line = len(list_of_trees[0]) -1
trees_done = [[False]*len_of_line for i in range(len(list_of_trees))]

for i in range(len(trees_done)):
    max_so_far = -1
    #left-side
    for j in range(len_of_line):
        tree = int(list_of_trees[i][j])
        if max_so_far < tree:
            max_so_far = tree 
            trees_done[i][j] = True
            

    max_so_far = -1
    #right-side
    for j in reversed(range(len_of_line)):
        tree = int(list_of_trees[i][j])
        if max_so_far < tree:
            max_so_far = tree 
            trees_done[i][j] = True

for i in range(len_of_line):
    max_so_far = -1
    #left-side
    for j in range(len(trees_done)):
        tree = int(list_of_trees[j][i])
        if max_so_far < tree:
            max_so_far = tree 
            trees_done[j][i] = True

    max_so_far = -1
    #right-side
    for j in reversed(range(len(trees_done))):
        tree = int(list_of_trees[j][i])
        if max_so_far < tree:
            max_so_far = tree 
            trees_done[j][i] = True

res = 0
for i in range(len(trees_done)):
    for j in range(len_of_line):
        if trees_done[i][j] == True:
            res +=1
print("Part One: " + str(res))


#PART 2
def scenic_score(i, j):
    row_temp = i
    col_temp = j
    l, r, u, d = 0,0,0,0
    val = int(list_of_trees[i][j])

    #print(val)
    #print(int(list_of_trees[i][col_temp]))
    col_temp -=1 
    while col_temp >= 0:
        l += 1
        if val <= int(list_of_trees[i][col_temp]):
            break
        col_temp -= 1
    col_temp = j
    col_temp +=1 
    while col_temp < len_of_line:
        r += 1
        if val <= int(list_of_trees[i][col_temp]):
            break
        col_temp += 1
    row_temp -= 1
    while row_temp >= 0:  
        u += 1
        if val <= int(list_of_trees[row_temp][j]):
            break
        row_temp -= 1
    row_temp = i
    row_temp += 1
    while row_temp < len(list_of_trees):
        d += 1
        if val <= int(list_of_trees[row_temp][j]):
            break
        row_temp += 1
    return l * r * u * d
    
max_val = 0 
for i in range(len(trees_done)):
    for j in range(len_of_line):
        max_val = max(max_val, scenic_score(i,j))

print("Part Two: " + str(max_val))


