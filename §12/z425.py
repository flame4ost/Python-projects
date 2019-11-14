s = input("Enter s: ")
t = input("Enter t: ")

s = float(s)
t = float(t)

r = 0.0

def G(a, b):
    return ((pow(a, 2) + pow(b, 2))/(pow(a, 2) + 2 * a * b + 3 * pow(b, 2) + 4))

r = G(1.2, s) + G(t, s) - G(2 * s - 1, s * t)
print("Result %.2f" % r)