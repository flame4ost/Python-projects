n = input('N: ')
print(f'В числе {len(n)} цифр')
print(f'Сумма цифр: {sum(map(int, [_ for _ in n]))}')
print(f'Последняя цифра: {n[-1:]}')
print(f'Первая цифра: {n[:1]}')
if len(n) >= 2:
    print(f'Предпоследняя цифра: {n[-2:-1]}')
