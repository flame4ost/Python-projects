s = str(input("Введите строку: "))

ss = list(s)
n = len(s)

i = 0

print(ss)

for i in range(n):
    if ss[i] == '*':
        del ss[i]
    i = i + 1
print(ss)
