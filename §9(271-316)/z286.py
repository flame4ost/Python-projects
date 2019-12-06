ls = tuple(map(int, input('Введите числа через пробел = ').split(' ')))
m = max(ls)
ls2 = [i for i in ls if i != m]
print(*ls)
print(*ls2)
