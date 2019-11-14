import math
print("Задание 88(a) ")
n = input("Введите число n ")
n = int(n)
n = n*n
print("Число в квадрате = ", n)
f = False
while (n>0):
    if (n%10 == 3): f  = True
    n = n//10
if f:print("Число 3 найдено")
else:print("Число 3 не найдено")

print("Задание 88(b) ")
n = input("Введите число n ")
n = int(n)
print("N = ", n)
s = 0
while (n>0):
    i = n%10
    s = s*10+i
    n = n//10
print("Результат = ", s)


print("Задание 88(g) ")
n = input("Введите число n ")
n = int(n)
print("N = ", n)

b = n
r = 10
while b>0:
    b = b//10
    r = r*10
print("Результат",r+n*10+1)

print("Задание 88(v) ")
n = input("Введите число n ")
n = int(n)
print("N = ", n)
i = 1
while ((n%i)>0):
    i = i*10
i = i//10
first = n//i
last = n%10
r = ((((n%i)+last*i)//10)*10+first)
print("Результат",r)
