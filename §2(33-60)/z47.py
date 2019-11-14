x = input("Введите X: ")
y = input("Введите Y: ")
z = input("Введите Z: ")
x = float(x)
y = float(y)
z = float(z)
if ((x+y>z) or (x+z>y) or (y+z>x)) :
    if((x*x+y*y>z*z) or (x*x+z*z>y*y) or (z*z+y*y>x*x)): print ("Трикутник остоугольний")
    else: print("Трикутник не остоугольний")
else:  print("Трикутник не існує")
    
    
