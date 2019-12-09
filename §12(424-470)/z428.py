a = input("Enter a: ")
b = input("Enter b: ")

a = int(a)
b = int(b)

def min(x, y):
    if (x>=y):
        f = x
    if (y>=x):
        f = y
    return f

u = min(a, b)
print("U = %.2f" % u)

v = min(a * b, a + b)
print("V = %.2f" % v)

k = min(u + pow(v, 2), 3.14)
print("Minimum %.2f" % k)