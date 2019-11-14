import math
print("Задание 111 ")
x = input("Введите х ")
x = int(x)
i=256
result = pow(x,2)
while i>=2:
    result = (pow(x,2)+(i/result))
    i=i/2
print("Результат",x/result)
