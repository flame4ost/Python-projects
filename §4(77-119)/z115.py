import math
print("Задание 115a ")
n = input("Введите n ")
n = int(n)
print("n = ",n)
s = 0
k = 1
for k in range(1, n):
    s = s + (1/k)
print("Сумма",s)

print("Задание 115 б ")
n = input("Введите n ")
n = int(n)
print("n = ",n)
s = 0
k = 1
for k in range(1, n):
    s = s + (math.exp(5*(math.log(k))))
print("Сумма",s)

print("Задание 115 в ")
n = input("Введите n ")
n = int(n)
print("n = ",n)
s = 0
k = 1
for k in range(1, n):
    s = s + 1 + (pow(2*k+1,2))
print("Сумма",s)

print("Задание 115 г ")
n = input("Введите n ")
n = int(n)
print("n = ",n)
s = 0
k = 1
for k in range(1, n):
    if (k%2) == 0:
        znak = 1
    else: znak = -1
s = s + znak / (k*(2*k+1))
print("Сумма",s)

print("Задание 115 д ")
n = input("Введите n ")
n = int(n)
print("n = ",n)
s = 0
k = 1
for k in range(1, n):
    if ((k%2)<0 and (k%2>0)):
        znak = 1
    else: znak = -1
s = s + znak / (k*(k+1))
print("Сумма",s)

print("Задание 115 e ")
n = input("Введите n ")
n = int(n)
print("n = ",n)
s = 0
k = 1
i =1
for k in range(i):
    i = k*i
    for i in range(1,n):
        if (i%2) == 0:
            znak = 1
        else: znak = -1
s = s + (znak * (k+1))/i
print("Сумма",s)

print("Задание 115 ж ")
n = input("Введите n ")
n = int(n)
print("n = ",n)
s = 0
z = 0
ch = 1
i =1
for i in range(1,n):
    ch = ch * i
    z = z+1/(i+1)
    s = s + (ch/z)
print("Результат",s)
