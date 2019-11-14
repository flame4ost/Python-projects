import math
print("Задание 84 a")
n = input("Введите число n ")
n = int(n)
x = input("Введите число x ")
x = int(x)
print("n=",n)
print("x=",x)
s = 0
i = 1
for i in range(n):
    s = s + (math.exp(i*(math.log(math.sin(x)))))
print("Suma = ",s )

print("Задание 84 б")
n = input("Введите число n ")
n = int(n)
x = input("Введите число x ")
x = int(x)
print("n=",n)
print("x=",x)
s = 0
i = 1
for i in range(n):
    s = s + (math.sin(math.exp(i*(math.log(x)))))
print("Suma = ",s )

print("Задание 84 в")
n = input("Введите число n ")
n = int(n)
x = input("Введите число x ")
x = int(x)
print("n=",n)
print("x=",x)
s = 0
i = 1
sinus = 1
for i in range(n):
    sinus = (math.sin(sinus*x))
    s = s + sinus
print("Suma = ",s )
