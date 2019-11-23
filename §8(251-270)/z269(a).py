import re
s = 'Hello, R2D2: how; are you?'
w = len(re.findall('\w+', s))
print(w)
