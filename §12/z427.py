a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")

a = int(a)
b = int(b)
c = int(c)

f = -999999999

def max(x, y, z):
    if (x>=y) and (x>=z):
        f = x
    if (y>=x) and (y>=z):
        f = y
    if (z>=x) and (z>=y):
        f = z
    return f
r = (max(a, a + b, f) + max(a, b + c, f)) / (1 + max(a + b * c, 1, 15))
print("Result %.2f" % r)