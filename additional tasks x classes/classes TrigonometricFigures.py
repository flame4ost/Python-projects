# -*- coding: utf-8 -*-
 
import math
import msvcrt
 
class Cube:
 
    def __init__(self, edge:float):
        self.edge = edge
 
    def area(self):
        return self.edge**2 * 6
 
    def bulk(self):
        return self.edge**3
 
class Cylinder:
 
    def __init__(self, radius:float, height:float):
        self.radius, self.height = radius, height
 
    def area(self):
        return 2 * math.pi * self.radius * (self.height + self.radius)
 
    def bulk(self):
        return math.pi * self.radius**2 * self.height
 
class Tetrahedron:
 
    def __init__(self, edge:float):
        self.edge = edge
 
    def area(self):
        return 3**(1/2) * self.edge**2
 
    def bulk(self):
        return 3**(1/2) / 12 * self.edge**3
 
def main():
    print("""Выбирите номер фигуры:
        1) Куб
        2) Цилиндр
        3) Тетраэдер""")
 
    while True:
        key = msvcrt.getch()
        if key in [b"1", b"2", b"3"]: break
 
    if key == b"1":
        figure = Cube(float(input("Ребро: ")))
    elif key == b"2":
        figure = Cylinder(float(input("Радиус: ")), float(input("Высо3та: ")))
    elif key == b"3":
        figure = Tetrahedron(float(input("Ребро: ")))
    else:
        raise KeyError
 
    print("""Выбирите номер параметра:
        1) Площадь
        2) Объем""")
 
    while True:
        action = msvcrt.getch()
        if action in [b"1", b"2"]: break
 
    if action == b"1":
        print(f"Площадь фигуры: {figure.area():.2f}")
    elif action == b"2":
        print(f"Объем фигуры: {figure.bulk():.2f}")
    else:
        raise KeyError
 
if __name__ == '__main__':
    main()
