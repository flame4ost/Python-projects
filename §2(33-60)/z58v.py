a = input ("input a: ")
f = 0.0

a = float(a)

if (a <= 0):
    f = abs(a+1)
else:
    f = abs(a-1)
print ("f = %.2f" % f)
