from math import floor
 
x = float(input('X: '))
print(f'Ближайшее целое = {round(x)}')
print(f'Без дробных цифр = {int(x)}')
print(f'Часть числа = {floor(x)}')

