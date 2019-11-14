import random
import math

n = 20

a = 0
i = 1
s = 1

while i <= n:
    a = random.randrange(0, 10)
    print("a = %.2f" % a)
    print(" ")

    if ((i + 1) < a) and (a < math.factorial(i)):
        s = s * a
    i = i + 1
k = 1/s

print("k = %.2f" % k)