def sum_div(n):
    s=1
    i=2
    while(i*i<=n):
        if n%i==0:
            s+=i
            j=n//i
            if j != i:
                s+=j
        i+=1        
    return s
    
def task(n):
    d=2
    max=2
    for i in range(2,n+1):
        s=sum_div(i)
        if s > max:
            max=s
            d=i
    return (d,s)
    
print(task(1000))
