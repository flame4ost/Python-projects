i, n, a, summ = int(input()), int(input()), list(map(int, input().split())), 0
for index, element in enumerate(a): summ += element if index != i else 0
print(summ / n)
