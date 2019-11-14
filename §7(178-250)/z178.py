from random import randint
print("Задание 178 а")
n = (int(input("Введите n = ")))
print(n)
k = 0
i = 1
for i in range(n):
    a = int(input(f"Введите {i} число "))
    if (a % 2 != 0):#
         k += 1
print("Результат ", k)
print("_________________________________")

print("Задание 178 б")
n = (int(input("Введите n = ")))
print(n)
k = 0
i = 1
for i in range(n):
    a = int(input(f"Введите {i} число "))
    print(a)
    if (a%3 == 0) and (a%5!=0):
        k += 1
print("Результат = ",k)
print("_________________________________")

#print("Задание 178 в")
#n = [randint(1, 1000) for i in range(500)]
#Q = 0
#i = 1
#print('Выводим последовельность ' ,n, 'случайных чисел ')
#for i in range(n):

print("Задание 178 г")

    
