import random

n = 100

a = 0
i = 1

for i in range(n):
    a = random.uniform(-500, 500)
    print("Before:")
    print("a = %.2f" % a)

    if a < 0:
        a = a + 0.5
    elif a > 0:
        a = 0.1
    print("After:")
    print("a = %.2f" % a)