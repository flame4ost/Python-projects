import random

n = 20

a = 0
i = 1
s = 0
k = 0

for i in range(n):
    a = random.uniform(0, 10)
    print("Before:")
    print("a = %.2f" % a)
    if a < 2:
        a = 1
    print("After:")
    print("a = %.2f" % a)

    if a >= 3 and a <= 7:
        s = s + a
        k = k + 1
print("Sum [3, 7]: %.2f" % s)
print("Kol [3, 7]: %.2f" % k)