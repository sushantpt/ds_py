mat = [[1,2,3,4], [3,4,2], [12,44,56], [12,342,23]]
sums_list = []
for i in range(len(mat)):
    total = 0
    for j in range(len(mat[i])):
        total = total + mat[i][j]
        sums_list.append(total)
print(sums_list)
