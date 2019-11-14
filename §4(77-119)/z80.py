import math
print ("Задание 80")
x = input("Введите число ")
x = int(x)
print("x=",x)
summa= 0
kvadrat = 1
fact = 1
i =1
for i in range (1, 13):
    kvadrat = kvadrat*x
    fact = fact*i
    if i%2 == 1:
        if i%4 == 3:
            summa = summa-kvadrat/fact
print("Ответ = ", summa) 
