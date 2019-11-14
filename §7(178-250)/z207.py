print("Задание 207")
n = (int(input("n = ")))
newN = 0
k = 1
while n!=0:
    number = n%10
    if (number!=5) and (number !=0):
        newN = newN + number * k
        k = k*10
    n = n//10
print("Результат = ",newN)

