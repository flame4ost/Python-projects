n=int(input("Enter N: "))
matrix = [[ randint(0,9) for _ in range(9)] for _ in range(n)]
 
for i in matrix:
    print(i)
 
means = [0 for x in range(4)] # 9 columned matrix will have 4 columns with even num (2,4,6,8)
 
for row in matrix:
    for i, col in enumerate(row[1::2]):
        means[i] += col/n
 
print(means)
