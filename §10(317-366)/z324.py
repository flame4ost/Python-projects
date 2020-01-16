import math
q = 12
p = 4
dividers = filter(lambda x: not q % x and math.gcd(x, p) == 1, range(1, q + 1))
print(*dividers)
