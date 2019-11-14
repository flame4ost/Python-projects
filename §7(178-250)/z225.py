def cm(m, n):
    for x in range(1, m*n):
        if x % m == 0 and x % n == 0:
            print ("Общие делители: " + str(x))
 
cm(6, 20)
