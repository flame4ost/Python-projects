import math
print ("Задание 23")
a = input("Введите число а ") 
a = float(a)
b = input ("Введите число b ")
b = float (b)
c = input ("Введите число c ")
c = float (c)
p = (a+b+c)/2
print ("Полупериметр = ", p)
H = (2*a)* math.sqrt(p*(p-a)*(p-b)*(p-c))
print ("Висота = ", H)
M = (1/2)* math.sqrt(2*a*a+2*b*b-c*c)
print ("Медиана = ", M)
L = (2*(math.sqrt(a*b*p*(p-c/(a+b)))))
print ("Длина бисектриси = ", L)
R_op = (a*b*c)/(4*(math.sqrt(p*(p-a)*(p-b)*(p-c))))
print ("Радиус описаного треугольника = ", R_op)
R_vp = (math.sqrt(p-a)*(p-b)*(p-c)/p)
print ("Радиус вписаного треугольника = ", R_vp)
