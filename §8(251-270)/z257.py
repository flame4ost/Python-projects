s = str(input("Введите строку. Первый символ не должен быть !"))

ss = list(s)
n = len(ss)

a = False
b = False
c = False
k = 0
i = 0
j = 0

for i in range(n):
    if s[i] == "!":
        break
    if s[i] == " ":
        k = k + 1
    if s[i] == "ю" or s[i] == "Ю":
        a = True
        print("A: " + a)
    if s[i] == "но" or s[i] == "он" or s[i] == "Но" or s[i] == "Он":
        b = True
        print("B: " + b)
    if s[i] == s[i+1]:
        c = True
        print("C: " + c)
print("Количество пробелов в строке: %.2f" % k)
