import random

n = 45

q = 0
i = 1
k = 0
o = 0

while i <= n:
    q = random.randrange(-20, 20)
    print("q = %.2f" % q)
    if i < 35 and q < 0:
        k = k + 1
    if q == 0:
        o = o + 1
    i = i + 1
print("k [1, 35] = %.2f" % k)
print("o [1, 45] = %.2f" % o)