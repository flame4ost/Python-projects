def task2(a):
    a1=a[0:10]
    a2=a[10:]
    return list(map(lambda x : max([x[0],x[1]]),zip(a1,a2)))+list(map(lambda x : min([x[0],x[1]]),zip(a1,a2)))
           
print(task2([1,2,6,7,2,4,0,11,7,9,0,2,12,23,-5,-2,3,6,7,-8,13])    )
