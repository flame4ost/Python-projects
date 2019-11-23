import re
from collections import Counter
d=input('Введите символ=>')
print(Counter( s[0] for s in re.findall(r"[\w']+", input('Введите строку=>')) if s[0] == d))
