import math
x = input ("Введіть x: ")
x = int(x)
y = input ("Введіть y: ")
y = int(y)
z = input ("Введіть z: ")
z = int(z)
if (x>y) and (x>z):
    print("Макимальное число = ", x)
elif (y>x) and (y>z):
    print("Макимальное число = ", y)
elif (z>y) and (z>x):
    print("Макимальное число = ", z)
x = input ("Введіть x: ")
x = int(x)
y = input ("Введіть y: ")
y = int(y)
z = input ("Введіть z: ")
z = int(z)
if (x<y) and (x<z):
    print("Минимальное число = ", x)
elif (y<x) and (y<z):
    print("Минимальное число = ", y)
elif (z<y) and (z<x):
    print("Минимальное число = ", z)
