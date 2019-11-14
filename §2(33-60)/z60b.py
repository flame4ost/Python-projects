x = input ("input x: ")
y = input ("input y: ")

u = 0.0

x = float(x)
y = float(y)

if ((y <= (x/2)) and ((y*y) >= (1-(x*x)))):
    u = -3
else:
    u = y*y
print ("u = %.2f" % u)
