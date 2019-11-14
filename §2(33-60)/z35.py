x = input("Input X: ")
y = input("Input Y: ")
z = input("Input Z: ")

x = int(x)
y = int(y)
z = int(z)

max1 = x + y + z
if ((x * y * z) > max1):
    max1 = x * y * z
print ("Result %.2f" % max1)

#########################################

min1 = x + y + z / 2
if ((x * y * z) < min1):
    min1 = x * y * z
min2 = ((min1*min1)+1)
print ("Result %.2f" % min2)
