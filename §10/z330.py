y = int(input('Укажите верхнюю границу: '))
x = int(input('Укажите нижнюю границу: '))

for i in range(x,y):
    s = 1
    j = 2
    while(j*j<=i):
        if i % j == 0:
            s += j
            k=i//j
            if j !=k:
                s+=k
        j+=1
    if s == i:
        print(i)
