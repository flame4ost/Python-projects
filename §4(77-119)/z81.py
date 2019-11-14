import math
x = input("Введите число х ")
x = int(x)
a = input("Введите число а ")
a = int(a)
n = input("Введите число n ")
n = int(n)
print("X=",x)
print("A=",a)
print("N=",n)
y = (x+a)**2
i = 0
for i in range(n):
    y = (y+a)**2
    y = y+a
print("Y = ",y)
