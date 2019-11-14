import random

n = 60

a = 0
i = 1
s = 0
k = 0

for i in range(n):
    a = random.randrange(0, 99)
    if (a % 5 == 0) and (a % 7 != 0):
        s = s + a
        k = k + 1
    i = i + 1
print("Sum = %.2f" % s)
print("Kol = %.2f" % k)