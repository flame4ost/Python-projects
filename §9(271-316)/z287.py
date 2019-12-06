import random
chisla = [random.randint(0,50) for i in range(20)]
maxchi = chisla.index(max(chisla))
res = []
 
for i, j in enumerate(chisla[0:maxchi]):
    if i % 2 == 0:
        res.append(j*max(chisla))
 
print(res)
