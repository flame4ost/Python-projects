import random

n = 10

a = 0
i = 1
k = 0

for i in range(n):
    a = random.randrange(0, 20)
    print("Before:")
    print("a = %.2f" % a)

    if a > 7:
        a = 7
        k = k + 1
    print("After:")
    print("a = %.2f" % a)
print("Kol = %.2f" % k)
