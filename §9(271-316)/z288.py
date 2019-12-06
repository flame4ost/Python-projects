def task(lst):
    if sum(list(map(lambda z: 0 if z[0]*z[1]<0 else 1,(zip(lst,lst[1:])))))==0:
        return lst
    else:
        return list(filter(lambda x: x<0,lst))
        
print(task([1,-1,5,-4,6,7]))
print(task([1,-1,5,-4,6,-7]))
