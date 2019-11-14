import random

n = 10

q = 0
i = 1
while True:
    c = int(input("1 = a, 2 = b, 0 = exit "))
    if c == 1:
        for i in range(n):
            q = random.randrange(0, 99)
            if (q//2) % 2 != 0:
                print(q)
    if c == 2:
        for i in range(n):
            q = random.randrange(0, 99)
            if ((q % 7) == 1) or ((q % 7) == 2) or ((q % 7) == 5):
                a = q % 7
            if ((q % 7) == 1) or ((q % 7) == 2) or ((q % 7) == 5):
                print("q = %.2f" % q)
                print("mod = %.2f" % a)
                print(" ")
    if c == 0:
        break