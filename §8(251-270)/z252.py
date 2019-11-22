s = str(input("Введите строку: "))

ss = list(s)

n = len(s)

k = 0
m = 0
f = 0

for i in range(n):
    if ss[i] == "+":
        k = k + 1
    if ss[i] == "*":
        m = m + 1
    if ss[i] == "-":
        f = f + 1
    i = i + 1

print(ss)
k = str(k)
m = str(m)
f = str(f)
print("Кол-во символов + в строке: " + k)
print("Кол-во символов * в строке: " + m)
print("Кол-во символов - в строке: " + f)
