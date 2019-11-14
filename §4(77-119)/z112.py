import math
print("Задание 112 ")
n = input("Введите n ")
n = int(n)
print("n = ",n)
result = 1
if (n%2) == 0:
    i = 2
else: i = 1
while (i<=n):
    result = result*i
    i = i+2
print("n!!",result)
