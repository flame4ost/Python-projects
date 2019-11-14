import math
print("Задание 88(b) ")
n = input("Введите число n ")
n = int(n)
print("n = ", n)
x=1
y=1
i = 2
s = x /(1+(abs(y)))
for i in range(n):
    y = x+y
    x = 0.3*x
    s=(s+(x*(1+(abs(y)))))
print("Sum = ",s)
