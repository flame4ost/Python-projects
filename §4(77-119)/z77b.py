import time
while True:
    start_time = time.time()
    n = print("Введите число n ")
    if (n == "exit"):
        break
    else :
        n = int(input())
        factorial = 1
        for i in range(2, n+1): 
            factorial *= i
    print("Факториал = ", factorial)
    print("--- %s seconds ---" % (time.time() - start_time))
