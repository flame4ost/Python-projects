import math
n = (int(input("Введите число n ")))
i = 3
for i in range(n):
    x = i*i*i-3*i*n*n+n
    print(i,'. ',x)
    if (frac(x/3)==0) and (odd(round(x//3))):
        s = s+x
        print(x, ' - утроенное нечетное')
print("s = ", s)
