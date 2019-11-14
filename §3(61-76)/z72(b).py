import math

def f(a):
    if a<=0:
        f=(-a)+1
    else:
        f=1-a*a*a
    return f
x = float(input("Enter x: "))
if x>1:
    while x>1:
        x=x-2
elif x<=(-1):
    while x<=(-1):
        x=x+2
print("y= %.2f" % f(x))