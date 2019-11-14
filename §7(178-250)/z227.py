print("Задание 227")
a = (int(input("Введите число a ")))
b = (int(input("Введите число b ")))
if a<b:
    m = a
else:m = b
for i in range(1,m):
    if a % i == 0 and b % i == 0:
        z = i
print(z)
