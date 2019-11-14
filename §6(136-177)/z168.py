import random
a = [random.randint(0,100) for i in range(37)]
flag = False
print(a)
for i in range(0,37):
    if a[i]>0:
        flag = True
    if flag:
        a[i] = a[i]-0.5
print(a)
