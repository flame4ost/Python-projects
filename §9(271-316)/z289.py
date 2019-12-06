from random import randint as rn
m=int(input())-1
a=[rn(-30,30) for _ in range(30)]
print(*a,'\n')
a[a.index(max(a))], a[m] = a[m], a[a.index(max(a))]
print(*a)
