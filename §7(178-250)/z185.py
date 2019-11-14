print("Задание 185")
n = (int(input("Введите число n ")))
s = 0
i = 1
for i in range(n):
    k = (int(input("Число = ")))
    if k > 0:
        s = s+k
print(2*s)
