a = input ("input a: ")
f = 0.0
a= float(a)

if(a<0):
    f = a * (-1)
elif(a<1):
    f = a
elif(a<2):
    f = 1.0
else:
    f = (5-(2*a))
print ("f = %.2f" % f)
