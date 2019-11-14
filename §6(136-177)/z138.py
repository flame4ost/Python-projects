from random import randint
 
mass = [randint(0, 10) for i in range(70)]
print(mass)
mass.append(mass[0])
mass.remove(mass[0])
print(mass)
