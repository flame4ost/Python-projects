import math

a = input("Введите a: ")
b = input("Введите b: ")
c = input("Введите c: ")
d = input("Введите d: ")
a = float(a)
b = float(b)
c = float(c)
d = float(d)
if ((a<=b) and (b<=c) and (c<=d)):
    a = d
    b = d
    c = d
elif ((a>b) and (b>c) and (c>d)):
      a = a*a
      b = b*b
      c = c*c
      d = d*d
print ("A = ",a , "B = ", b, "C = ", c, "D = ", d)
