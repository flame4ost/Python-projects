import random
 
random.seed(30)  #?
arr = [random.randint(0, 10) for _ in range(20)]
print(*arr)
 
s = sum(arr)
b = []
sz= len(arr)-1
for i in arr:
    b.append((s - i) / sz)
print(*b)
