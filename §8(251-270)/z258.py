import re
 
def prost():
    a=input()
    line = re.sub('[abcde]', '', a)
    print(line)
prost()
