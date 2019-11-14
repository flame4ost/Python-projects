print("Задание 156 б")
n = int(input("Введите n = "))
print("n = ",n)
i = 3
s = 0
x1 = int(input("Введите x1 = "))
x2 = int(input("Введите x2 = "))
for i in range(n):
    print(' x ',i, ' = ')
    x3 = int(input())
    s += (x1+x2+x3)*x2
    x1 = x2
    x2 = x3
print("Сумма = ",s)
