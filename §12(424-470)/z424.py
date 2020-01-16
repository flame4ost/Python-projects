
import math

s = input("Enter s: ")
t = input("Enter t: ")

s = float(s)
t = float(t)

r = 0.0

def F(a, b, c):
    return (2 * a - b - math.sin(c)) / (5 + abs(c))


r = F(t, -2*s, 1.17)+F(2.2, t, s-t)
print("Result: %.2f" % r)
