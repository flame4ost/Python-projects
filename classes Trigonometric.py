import math


# абстрактный класс фигура
class Figure:
    def __init__(self):
        pass

    # периметр
    def getPerimetr(self):
        pass

    # площадь
    def getArea(self):
        pass

    # вывод
    def print(self):
        pass


# класс прямоугольник
class Rectangle(Figure):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    # геттеры и сеттеры
    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        if a > 0:
            self.__a = a
        else:
            self.__a = 0

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        if b > 0:
            self.__b = b
        else:
            self.__b = 0

    # периметр
    def getPerimetr(self):
        return 2 * (self.__a + self.__b)

    # площадь
    def getArea(self):
        return self.__a * self.__b

    # вывод
    def print(self):
        print("Rectangle")
        print("A = ", self.__a)
        print("B = ", self.__b)
        print("Perimetr = ", self.getPerimetr())
        print("Area = ", self.getArea())


# круг
class Circle(Figure):
    def __init__(self, r):
        self.__r = r

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, r):
        if r > 0:
            self.__r = r
        else:
            self.__r = 0

    def getPerimetr(self):
        return 2 * 3.14 * self.__r

    def getArea(self):
        return 3.14 * self.__r * self.__r

    def print(self):
        print("Circle")
        print("R = ", self.__r)
        print("Perimetr = ", self.getPerimetr())
        print("Area = ", self.getArea())


# квадрат
class Square(Figure):
    def __init__(self, a):
        self.__a = a

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        if a > 0:
            self.__a = a
        else:
            self.__a = 0

    def getPerimetr(self):
        return 4 * self.__a

    def getArea(self):
        return self.__a * self.__a

    def print(self):
        print("Square")
        print("A = ", self.__a)
        print("Perimetr = ", self.getPerimetr())
        print("Area = ", self.getArea())


# триугoльник
class Triangle(Figure):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        if a > 0:
            self.__a = a
        else:
            self.__a = 0

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        if b > 0:
            self.__b = b
        else:
            self.__b = 0

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        if c > 0:
            self.__c = c
        else:
            self.__c = 0

    def getPerimetr(self):
        return self.__a + self.__b + self.__c

    def getArea(self):
        p = (self.__a + self.__b + self.__c) / 2
        return math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))

    def print(self):
        print("Triangle")
        print("A = ", self.__a)
        print("B = ", self.__b)
        print("C = ", self.__c)
        print("Perimetr = ", self.getPerimetr())
        print("Area = ", self.getArea())


# список обьектов
figures = list()
# вечный цикл
while (True):
    # вывод фигур
    print("\n\nFigures list:")
    if len(figures) == 0:
        print("List is empty!")
    else:
        for obj in figures:
            obj.print()
            print("\n")

    # меню
    print("1. Add")
    print("2. Exit")
    print(" < ")

    menu = int(input())

    # реализация меню
    print("\n")
    if menu == 1:
        print("1. Rectangle")
        print("2. Circle")
        print("3. Triangle")
        print("4. Square")

        choose = int(input())

        if choose == 1:
            print("A = ")
            a = int(input())

            print("B > ")
            b = int(input())

            figures.append(Rectangle(a, b))
        elif choose == 2:
            print("R > ")
            r = int(input())

            figures.append(Circle(r))
        elif choose == 3:
            print("A > ")
            a = int(input())

            print("B > ")
            b = int(input())

            print("C > ")
            c = int(input())

            figures.append(Triangle(a, b, c))
        else:
            print("A > ")
            a = int(input())

            figures.append(Square(a))
    elif menu == 2:
        break