import math
print ("Задание 18: Треугольник задан величинами своих углов и радиусом описанной окружности. Найти стороны треугольника.")
A = input("Введите угол A ") 
A = float(A)
B = input ("Введите угол B ")
B = float (B)
R = input ("Введите радиус ")
R = float (R)
C = 180 - A - B
a = 2 * R * math.sin(A * (math.pi/180))
b = 2 * R * math.sin(B * (math.pi/180))
c = 2 * R * math.sin(C * (math.pi/180))
print ("Сторона а =  ", a)
print ("Сторона b =  ", b)
print ("Сторона c =  ", c)

input ("Нажмите ENTER для выхода")
