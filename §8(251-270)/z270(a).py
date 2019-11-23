import re
a=str(input('Введите текст : '))
print(list(filter(None, re.split('\W|\d', a))))
