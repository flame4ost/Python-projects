k, m = map(int, input('Введите 2 целых числа: ').split())
x, y, z = map(float, input('Введите 3 вещественных числа: ').split())
if k < m * m:
    x = abs(x)
    y -= .5
    z -= .5
elif k == m * m:
    x -= .5
    y = abs(y)
    z -= .5
else:
    x -= .5
    y -= .5
    z = abs(z)
print(f'x = {x}, y = {y}, z = {z}')
