import math

while (True):
    print("1: Решить уравнение")
    print("2: Выйти из программы")

    m = int(input("Выберите пункт меню: "))

    if (m == 1):
        print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))

        discr = b ** 2 - 4 * a * c
        print("Дискриминант D = %.2f" % discr)

        if discr > 0:
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
            continue
        elif discr == 0:
            x = -b / (2 * a)
            print("x = %.2f" % x)
            continue
        else:
            print("Корней нет")
            continue
    if (m == 2):
        break
    else:
        print("Выбран неправильный пункт меню")
        continue