import math
print("Задание 88(b) ")
a = input("Введите число a ")
a = int(a)
b = input("Введите число b ")
b = int(b)
n = input("Введите число n ")
n = int(n)
print("n = ", a)
print("n = ", b)
print("n = ", n)
f = 0
h = (b-a)/n
i = 1
for i in range(n):
    f = f+(a+(i-1/2)*h)/(1+(pow(a+(i-1/2),2)*h))
    f = f*h
print("f = ",f)
