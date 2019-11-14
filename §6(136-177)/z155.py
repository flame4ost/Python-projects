print("Задание 154")
x = [i for i in range(1,101)]
n = int(input("Введите n>=2 = "))
print("n = ",n)
i = 1
for i in range(n):
    print('x[',i,']= ')
    print(x[i])
pr = 1
for i in range(n-1):
    if (abs(x[i]+1)>0): 
        pr = pr * (1/abs(x[i]+1)+x[i+1])
    else:print("Деление на ноль")
print("Выражение = ", pr)
