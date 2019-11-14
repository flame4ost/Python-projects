import math

n = int(input("Enter n: "))

k = 0
f = 1

sum = 0.0

while k <= n:
    if k:
        f *= k
    sum += math.pow(-1, k * (k - 1) * 2) / f
    k = k + 1
print("Sum = %.2f" % sum)