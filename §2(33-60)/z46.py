import math

a = input ("input a: ")
b = input ("input b: ")

a = float(a)
b = float(b)

if ((a < 0) and (b < 0)):
    a=  abs(a)
    b = abs(b)
elif ((a < 0) or (b < 0)):
    a = a + 0.5
    b = b + 0.5
elif ((a >= 0) and (b >= 0)):
    if ((a > 2.0) or (a < 0.5) and (b > 2.0) or (b < 0.5)):
        a = a / 10
        b = b / 10
print ("a = %.2f" % a)
print ("b = %.2f" % b)
