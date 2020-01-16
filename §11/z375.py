max = (0, 0)
 
for i in range(n):
    for j in range(n):
        if math.fabs(matrix[i][j]) > math.fabs(matrix[max[0]][max[1]]):
            max = i, j
 
new_matrix = []
 
for i in range(n):
    if i == max[0]:
        continue
 
    row = []
 
    for j in range(n):
        if j == max[1]:
            continue
 
        row.append(matrix[i][j])
 
    new_matrix.append(row)
