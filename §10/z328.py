i=2             
a = 0                     
bool_off = True
while bool_off:
    f=True
    j=2
    while f and j<i:
        if not i%j: f=False  
        j+=1
    if f: 
        print(i,end=' ')
        a += 1
    i+=1
    if a >= 100:
        bool_off = False
