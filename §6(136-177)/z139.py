import math
print("Задание 139 б")
n = int(input("n = : "))
i = 1
for i in range(n):
    rez  = n*n
print("Квадрат = "rez)

print("Задание 139 г")
n = int(input("n = : "))
b = 2
i = 1
for i in range(n):
    b = b*2
    print ('b',i,'=',b)

print("Задание 139 и")
p = 1
a = [i for i in range(1,21)]
n = int(input("n = : "))
a[1] = 1/p
print(a[1])
i = 2
for i in range(1,n):
    p = p*i
    a[i] = a[i-1]+1/p
print(a[i])

print("Задание 139 д")
a = [i for i in range(n)]
i = 1
for i in range(n):
    a[i] = (math.exp(2*i))+(math.exp(3*(i+1)))
    print(a[i])

