k = int(input("Enter k: "))
l = int(input("Enter l: "))

if k != l:
    if k > l:
        l = k
    else:
        k = l
else:
    k = 0
    l = 0
print("k = " + str(k) + " l = " + str(l))