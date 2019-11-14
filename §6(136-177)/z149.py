print("Задание 149")
xn = -3
xk=1
h = 0.1
x = xn
while x<=xk:
    y = 4 * x * (pow(x,2))-2*(pow(x,2))+5
    print("x = ",x,"y = ",y)
    x = x+h
