import math
print("Задание 77 а")
a = int(input("Число: "))
n = int(input("Степень: ")) 
i = 1
p = 1
for i in range(n):
    p = p*a
if a<0: p = 1/p
print("Число",p)

print("Задание 77 б")
n = int(input("Введите число "))
 
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(factorial)

print("Задание 77 г")
n = int(input("Введите число "))
s = 0
z = 0
i = 1
for i in range(n):
    z = z + (math.sin(n))
    s = s + 1/z
print("Сумма",s)

print("Задание 77 д")
n = int(input("Введите число "))
result = 0
i = 0
for i in range(n):
    result = (math.sqrt(2+result))
print("Результат",result)

print("Задание 77 ж")
n = int(input("Введите число "))
result = 0
for n in range(n):
    result = (math.sqrt(3*(i+result)))
    
print("Результат",result)
