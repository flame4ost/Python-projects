s = str(input("Введите строку: "))

ss = list(s)

n = len(s)

k = 0

for i in range(n):
    if ss[i] == "x":
        k = k + 1
    i = i + 1

print(s)
k = str(k)
print("Кол-во символов х в строке: " + k)
