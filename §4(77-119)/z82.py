import math
x = input("Введите число х ")
x = float(x)
print("X=",x)
znam = 1
chus = 1
i = 1
for i in range(6):
    chus = chus * (x-(math.exp(math.log(2)*i)))
    znam = znam * (x-(math.exp(math.log(2)*i)-1))
    dob = chus/znam
print("Добуток = ",dob)
