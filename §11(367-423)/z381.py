from random import randint
 
n = 10
 
matrix = [[randint(-10, 10) for _ in range(n)] for _ in range(n)]
 
for row in matrix:
    print(row)
 
max_item = max([item for row in matrix for item in row])
print('=================================')
print(max_item)
print('=================================')
 
for row in matrix:
    for i, item in enumerate(row):
        if item == max_item:
            row[i] = 0
    print(row)
