from fractions import gcd
def cm(m, n):
    for x in range(1, m*n):
        if x % m == 0 and x % n == 0:
            print ("common multiple: " + str(x))
 
cm(10, 15)
