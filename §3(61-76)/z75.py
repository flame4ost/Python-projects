import math
def gcd_ext( a, b ):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return x0, y0, b
#----------------------------------------
def any_solution( a, b, c ) :
    x0, y0, g  = gcd_ext( abs(a), abs(b) )
    if ( c % g != 0 ):
        return false;
    x0 = x0 * c // g;
    y0 = y0 * c // g;
    if a < 0 :
        x0 = -x0
    if b < 0 :
        y0 = -y0
    return x0, y0, g
#----------------------------------------    
def positive_solution( a, b, c ) :
    x, y, g = any_solution( a, b, n )
    while ( x < 0 ):
        x = x + b // g
        y = y - a // g
    while ( y < 0 ):
        x = x - b // g
        y = y + a // g    
    return x, y     
#----------------------------------------
a = 3
b = 5
n = 101
x, y = positive_solution( a, b, n ) 
print( x, "*", a, " + ", y, "*", b, " = ", n )
