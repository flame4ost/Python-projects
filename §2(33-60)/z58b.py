import math

a = input ("input a: ")

f = 0.0

a = float(a)

if (a < -1):
    f = (1/(a*a))
elif ((a >= -1) and (a <=2)):
    f = (a*a)
else:
    f = 4
print ("f = %.2f" % f)
