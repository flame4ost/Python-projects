print ("Задание 24: Вычислить расстояние между двумя точками с координатами x1, y1 и x2, y2")

import math

x1 = input ("Введите x1: ")
y1 = input ("Введите y1: ")

x2 = input ("Введите x2: ")
y2 = input ("Введите y2: ")

x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)

d = (math.sqrt((x2-x1)**2+(y2-y1)**2))

print ("Расстояние между точками %.2f" % d)

input ("Нажмите ENTER для выхода")
