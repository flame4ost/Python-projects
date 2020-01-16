import math
n = 1
while True:
    res = []
    for x in range(1, n):
        for y in range(1, n):
            r = x ** 3 + y ** 3
            if r == n:
                res.append((x, y))
            elif r > n:
                break
    if len(res) > 1:
        print(res, n)
        break
    n += 1
