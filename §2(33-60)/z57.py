import math
print ("Задание 57(а)")
a = input("Введите a: ")
a = float(a)
if (a>=-2 and a<2):
    f = a*a
else: f =4
print ("f(a) = ", f)

print ("Задание 57(б)")
a = input("Введите a: ")
a = float(a)
if (a<=2):
    f = a*a+4*a+5
else: f = (1/(a*a))+ 4*a+5
print ("f(a) = ", f)

print ("Задание 57(в)")
a = input("Введите a: ")
a = float(a)
if (a<=0):
    f = 0
elif (0<a<=1): f = a
else: f = a*a*a*a
print ("f(a) = ", f)

print ("Задание 57(г)")
a = input("Введите a: ")
a = float(a)
if (a<=0):
    f = 0
elif (0<a<=1): f = (a*a)-a
else: f = (a*a)-(math.sin(3.14*(a*a)))
print ("f(a) = ", f)
