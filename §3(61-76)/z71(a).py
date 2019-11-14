import math
def f(x):
    x0=math.fmod(x, 1.5)
    k = x0*x0*x0-2.5*x0
    return k
l = float(input())
print("F(x) = %.2f" % f(l))

