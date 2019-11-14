import math
print("Задание 114(a) ")
n = input("Введите n ")
n = int(n)
print("n = ",n)
result = 1
i = 1
for i in range(1, n):
    result = (result * (1/(i**2)))
print("n!!",result)

print("Задание 114(b) ")
n = input("Введите n ")
n = int(n)
print("n = ",n)
result = 1
i = 1
while n>=i:
    result = result +1/(math.exp(3*(math.log(i))))
    i = i+1
print("Результат = ",result)

print("Задание 114(c) ")
n = input("Введите n ")
n = int(n)
print("n = ",n)
result = 1
i = 1
f = 1
for i in range(1,n):
    f = f*i
    result = result + (1/f)
print("Результат = ",result)

print("Задание 114(g) ")
n = input("Введите n ")
n = int(n)
print("n = ",n)
result = 1
i = 1
for i in range(1,n):
    result = result + 1/(pow(2*i,2))
print("Результат = ",result)

print("Задание 114(d) ")
n = input("Введите n ")
n = int(n)
print("n = ",n)
result = 1
i = 1
for i in range(1,n):
    result = result * (pow(i,2)/(pow(i,2)+((2*i)+3)))
print("Результат = ",result)

print("Задание 114(e) ")
n = input("Введите n ")
n = int(n)
print("n = ",n)
result = 1
i = 1
f = 1
for i in range(1,n):
    f = f*i
    result = (result * (2+(1/f)))
print("Результат = ",result)

print("Задание 114(j) ")
n = input("Введите n ")
n = int(n)
print("n = ",n)
result = 1
i = 2
for i in range(1,n):
    result = result * ((i+1)/(i+2))
print("Результат = ",result)

print("Задание 114(z) ")
n = input("Введите n ")
n = int(n)
print("n = ",n)
result = 1
f = 1
i = 2
for i in range(1,n):
    f = f*i
    result = result * (pow(1 * 1/f,2))
print("Результат = ",result)
