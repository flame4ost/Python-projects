import random

n = int(input("Enter n "))
p = int(input("Enter p "))

a = 0
i = 1
s = 1

for i in range(n):
    a = random.randrange(0, 999)
    if a % p == 0:
        s = a * s
    i = i + 1
print("S = %.2f" % s)