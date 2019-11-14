import math

a = input("Input A: ")
b = input("Input B: ")
c = input("Input C: ")

a = float(a)
b = float(b)
c = float(c)

if ((a >= b)and(b >= c)):
    a = a * 2
    b = b * 2
    c = c * 2
else:
    a = abs(a)
    b = abs(b)
    c = abs(c)
print ("A: %.2f" % a)
print ("B: %.2f" % b)
print ("C: %.2f" % c)
