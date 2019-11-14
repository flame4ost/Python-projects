import cmath 
print("Задание 154")
x = [i for i in range(1,21)]
y = [i for i in range(1,21)]
n = int(input("Введите количество домов = "))
print("n = ",n)
a = (int(input("Введите координату школи а = ")))
print("a = ",a)
b = (int(input("Введите координату школи b = ")))
print("b = ",b)
print("Введите коордиаты домов")
i = 1
for i in range(n):
    print(x[i],y[i])
print("Расстояния от домов до школы")
s = 0
for i in range(n):
    r = (cmath.sqrt(a-x[i]**2)+(b-y[i]**2))
    print('Дом',i,'= ',r)
    s = s+r
s = s/n
print("Среднее арифетическое = ",s)
