def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
        
def task(n):
    r=[]
    for i in range(2,n):
        if gcd(i,n)==1:
            r+=[i]
    return r
        
print(task(100))
