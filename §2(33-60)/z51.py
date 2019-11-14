import math
print ("Задание 51 ")
c = input("Введите c: ")
b = input("Введите b: ")
a = input("Введите a: ")
c = float(c)
b = float(b)
a = float(a)
if (a==0):
    if(b!=0):
        if(c==0):print("X=0")
        elif (c/b<0):
                x1=(math.sqrt(-(c/b)))
                x2=(-math.sqrt(-(c/b)))
                print("X1 = ", x1, "X2 = ", x2)
else:
    print("Нет решений")
if c!=0:
    print ("Нет решений")
else:
    print("X любое")
D = ((b*b)-4*a*c)
if D<0:
    print("Нет решений")
else:
    d = (math.sqrt(D))
    t1 = (-b+d)/2*a
    t2 = (-b-d)/2*a
if t1>0:
    x1 = (math.sqrt(t1))
    x2 = (-math.sqrt(t1))
    print("X1 = ", x1, "X2 = ", x2)
    log = true
if t2>0:
    x3 = (math.sqrt(t2))
    x4 = (-math.sqrt(t2))
    if log==true:
        print("X3 = ",x3 , "X4 = ",x4)
    if log==false:
        print("X1 = ",x2, "X2 = ",x2)
