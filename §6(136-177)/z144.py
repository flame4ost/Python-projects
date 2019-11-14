print("Задание 144")
n = int(input("n = : "))
print("n = ",n)
print("Последовательность un: ")
u0 = 0
u1=1
print("u0 = ",u0,"u1 = ",u1)
i = 1
for i in range(n-1):
    buf = u1
    u1 = u0+u1
    u0 = buf
    print("u1 = ",u1)
print("Последовательность fn: ")
f0 = 0
f1 = 1
u0 = 0
u1 = 1
print("f0 = ",f0,"f1 = ",f1)
for i in range(n-1):
    buf = f1
    f1 = f0 + f1 + u0
    f0 = buf
    buf1 = u1
    u1 = u0+u1
    u0 = buf1
    print("f1 = ", f1)
