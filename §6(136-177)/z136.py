while True:
    print("Выберите действие:")
    print("1 - a1+....+an")
    print("2 - a1*....*an")
    print("3 - |a1|+....+|an|")
    print("4 - |a1|*....*|an|")
    print("5 - a1^2+....+an^2")
    print("6 - a1+....+an, a1*....*an")
    print("0 - Выход")
    m = int(input())
    if m == 1:
        n = int(input("Введите количество значений: "))

        i = 1
        k = 0

        while i <= n:
            print("Введите значение " + str(i) + ":")
            a = float(input())
            k = k + a
            i = int(i)
            i = i + 1
        print("a1+....+an = " + str(k))
        print(" ")
    if m == 2:
        n = int(input("Введите количество значений: "))

        i = 1
        k = 1

        while i <= n:
            print("Введите значение " + str(i) + ":")
            a = float(input())
            k = k * a
            i = int(i)
            i = i + 1
        print("a1*....*an = " + str(k))
        print(" ")
    if m == 3:
        n = int(input("Введите количество значений: "))

        i = 1
        k = 0

        while i <= n:
            print("Введите значение " + str(i) + ":")
            a = float(input())
            k = k + abs(a)
            i = int(i)
            i = i + 1
        print("|a1|+....+|an| = " + str(k))
        print(" ")
    if m == 4:
        n = int(input("Введите количество значений: "))

        i = 1
        k = 1

        while i <= n:
            print("Введите значение " + str(i) + ":")
            a = float(input())
            k = k * abs(a)
            i = int(i)
            i = i + 1
        print("|a1|*....*|an| = " + str(k))
        print(" ")
    if m == 5:
        n = int(input("Введите количество значений: "))

        i = 1
        k = 0

        while i <= n:
            print("Введите значение " + str(i) + ":")
            a = float(input())
            k = k + a**2
            i = int(i)
            i = i + 1
        print("a1^2+....+an^2 = " + str(k))
        print(" ")
    if m == 6:
        n = int(input("Введите количество значений: "))

        i = 1
        k = 0
        s = 1

        while i <= n:
            print("Введите значение " + str(i) + ":")
            a = float(input())
            k = k + a
            s = s * a
            i = int(i)
            i = i + 1
        print("a1+....+an = " + str(k))
        print("a1*....*an = " + str(s))
        print(" ")
    if m == 0:
        break
    else:
        print("Пожалуйста введите правильное значение!")
        print("")