print("Задание 145 а ")
x1 = 0
x2 = 5.0/8.0
print(x1,x2)
i = 3
for i in range(1,21):
    x = (x2/2)+(3/4)*x1
    print(x)
    x1 = x2
    x2 = x
print("___________________________________________")

print("Задание 145 в ")
s = 0
x1 = 1
x2 = 3/10
i = 3
for i in range(1,21):
    xi = (i+1)*x1
    x1 = x2
    x2 = xi
    s = s+xi
print("Сумма",s)
