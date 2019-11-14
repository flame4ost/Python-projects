import math
print("Задание 87 ")
n = input("Введите число n ")
n = int(n)
m = input("Введите число m ")
m = int(m)
print("n= ",n)
print("m= ",m)
s = 0
i = 1
for i in range(m):
    s = s + (n%10)
    n = n//10
    if(n==0):
        break
print("Cумма = ",s )

