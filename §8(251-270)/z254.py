nmax = 100
n = int(input(f'Количество символов от 2 до {nmax} n= '))
lst = (input() for _ in range(n))
if ',-' in ''.join(lst):
    print('Есть сочетание запятая+тире')
else:
    print('Нет сочетания запятая+тире')
