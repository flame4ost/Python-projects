import random
n = int(input("n = "))
n = 20
all = [random.randint(-10, 10) for i in range(n)]
print(all)
[-1, 3, -3, 1, 3, 6, 10, -3, -10, 10, 7, 0, -8, -4, 2, -4, 5, -7, 2, 6]
print(sum([i for i in all if i > 0]))
print(len([i for i in all if i < 0]))
