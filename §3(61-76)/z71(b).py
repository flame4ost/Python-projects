import math

def f(x):
    while x>1.5:
        x=x-1.5
    while x<0:
        x=x+1.5
    if x<=1:
        f=1.5*x-0.5
    else:
        f=3*x+4
    return f
a = float(input("Enter A: "))
print ("F(x)= %.2f" % f(a))
