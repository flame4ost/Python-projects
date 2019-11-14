import math
print("Задание 86 ")
a = input("Введите число a ")
a = int(a)
print("a= ",a)
b = a
k = 0
s = 0
c = None
while b>0:
    c = b%10
    k = k+1
    s = s+c
    b = b//10
print("Количество цифр = ",k )
print("Сумма = ",s )
print("Первая цифра = ", c)
