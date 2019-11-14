import math
print("Задание 83 a")
a = input("Введите число a>1 ")
a = float(a)
print("a=",a)
s = 0
i = 1
while s<=a:
    s+=1/i
    i+=1
print("S = ",s )

print("Задание 83 б")
a = input("Введите число a ")
a = float(a)
print("a=",a)
s = 1
n = 1
while s<a:
    n = n+1
    s = (s+(1/n))
print("Наименьешее n для которого s>a = ",n )
print("S = ",s )
