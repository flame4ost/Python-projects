import random

n = 50

a = 0
i = 1

while True:
    s = int(input("1 = a, 2 = b, 3 = c, 0 = Exit "))
    if s == 1:
        for i in  range(n):
            a = random.randrange(0, 99)
            if (a % 5) == 0:
                print("a = %.2f" % a)
        i = i + 1
    if s == 2:
        for i in  range(n):
            a = random.randrange(-99, 99)
            if a % 2 != 0 and a < 0:
                print("a = %.2f" % a)
        i = i + 1
    if s == 3:
        for i in  range(n):
            a = random.randrange(0, 99)
            if abs(a) < (i**2):
                print(a)
            i = i + 1
    if s == 0:
        break