from random import randint
import math
print("Задание 139 и")
a1 = int(input("a1 = : "))
a2 = int(input("a2 = : "))
a3 = int(input("a3 = : "))
a4 = int(input("a4 = : "))
print("a1 = ",a1,"a2 = ",a2,"a3 = ",a4,"a4 = ",a4)
i = 1
x = [randint(0, 50) for i in range(50)]
print (x)
b = ((x**2)-x-a1)*((x**2)*x-x-a2*(x-a3))/(x-a1)*(x-a2)-(x**2)/x    
print('b[',i,']= ',b,' при x[',i,']=',x)
