from operator import mul
from functools import reduce
 
n = int(input('N= '))
print(reduce(mul, ((x-0.5)/x for x in range(1, n+1))))
