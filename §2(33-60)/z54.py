import math
print ("Задание 54 ")
x1 = input("Введите x1: ")
y1 = input("Введите y2: ")
x2 = input("Введите x2: ")
y2 = input("Введите y2: ")
x3 = input("Введите x3: ")
y3 = input("Введите y3: ")
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
x3 = float(x3)
y3 = float(y3)
k1 = (math.sqrt(x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
k2 = (math.sqrt(0-x2)*(0-x2)+(0-y2)*(0-y2))
k3 = (math.sqrt(0-x1)*(0-x1)+(0-y1)*(0-y1))
k4 = (math.sqrt(0-x3)*(0-x3)+(0-y3)*(0-y3))
k5 = (math.sqrt(x3-x2)*(x3-x2)+(y2-y2)*(y3-y2))
k6 = (math.sqrt(x3-x1)*(x3-x1)+(y3-y1)*(y3-y1))
p1 = (k1+k2+k3)/2
p2 = (k2+k5+k4)/2
p3 = (k3+k4+k6)/2
p = (k1+k5+k6)/2
s1 = (math.sqrt(p1*(p1-k1)*(p1-k2)*(p1-k3)))
s2 = (math.sqrt(p2*(p2-k4)*(p2-k2)*(p2-k5)))
s3 = (math.sqrt(p3*(p3-k6)*(p3-k4)*(p3-k3)))
s4 = s1+s2+s3
s = (math.sqrt(p*(p-k1)*(p-k5)*(p-k6)))
if (s4==s): print("Начало координат принадлежит треугольнику ")
else: print("Начало координат не принадлежит треугольнику ")
