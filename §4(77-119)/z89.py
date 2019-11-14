import math
print("Задание 88 а ")
a = input("Введите число a ")
a = int(a)
b = input("Введите число b ")
b = int(b)
print("a = ", a)
print("b = ", b)
while (a and b):
    if a>=b:
        a = a-b
    elif(b>=a):
            b = b-a
print("Результат",b)

print("Задание 88 б")
def gcd(a,b):
    while(b>0):
        a,b=b,a%b
    return a
 
def lcm(x,y):
    return (x*y)//gcd(x,y)
 
a = int(input("Введите число a "))
b = int(input("Введите число b "))
print("Кратное = ",lcm(a,b))
