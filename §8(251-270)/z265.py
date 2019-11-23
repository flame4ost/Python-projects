from re import sub
print(sub(r'\*(.+)', lambda m: '*' + '_' * len(m.group(1)), input('Строка: ')))

