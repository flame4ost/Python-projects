while True:
    print("Выберите действие:")
    print("1 - a1, a1 + a2, ..., a1 + a2 + ... + an")
    print("2 - a1^2, a1*a2, ..., a1*an")
    print("3 - |a1|, |a1 + a2|, |a1 + ... + an")
    print("4 - a1, -(a1 * a2), a1 * a2 * a3, ..., (-1)^n+1 * a1 * a2 * ... * an")
    print("5 - -a1, a2, -a3, ..., (-1)^n * an")
    print("6 - a1 + 1!, a2 + 2!, ..., an + n!")
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
            print("k = " + str(k))
            i = int(i)
            k = int(k)
            i = i + 1
    if m == 2:
        n = int(input("Введите количество значений: "))

        i = 1
        k = 1

        while i <= n:
            print("Введите значение " + str(i) + ":")
            a = float(input())
            if i == 1:
                s = a
            k =  s * a
            print("k = " + str(k))
            i = int(i)
            k = int(k)
            i = i + 1
    if m == 0:
        break