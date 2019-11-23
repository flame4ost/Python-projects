s = '234ffg,fd,fd,g,dfg,df'
n = len(s)
for i in range(n):
    if s[i] == ',':
        print(i)
        break
