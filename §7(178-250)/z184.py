import random

n = 67

i = 1

while True:
    p = int(input("Enter p "))
    q = int(input("Enter q "))

    if not((q>0)and(p>q)):
        print("Prerequisite: P > Q > 0")
        print(" ")
    else:
        for i in range(n):
            a = random.randrange(-999, 999)
            print("Before:")
            print("a = %.2f" % a)
            print(" ")
            if abs(a) % p == q:
                a = 0
            print("After:")
            print("a = %.2f" % a)
            print(" ")
        break