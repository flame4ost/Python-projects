import math
c = 2
d = 4
dsc = 3**2 + 4 * (abs(c * d))
x1 = (3 + math.sqrt(dsc)) / 2
x2 = (3 - math.sqrt(dsc)) / 2
trunsf = 0
if x1 < x2:
    trunsf = x1
    x1 = x2
    x2 = trunsf
uravnen = 0.0
uravnen = abs((math.sin(abs( ( (c * x1)**3 + (d * x2)**2) - c*d ))**3) / ( math.sqrt(  (((c * x1)**3 + (d * x2)**2 ) - x1)**2 + 3.14  ) )   ) + (math.tan(((c * x1)**3 + (d * x2)**2 ) - x1))
print("Expression result =  ", uravnen)

