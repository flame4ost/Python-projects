string = input()
 
words = string.split()
 
shortest = words[0]
 
for i in words[1:]:
    if len(i) < len(shortest):
        shortest = i
 
print(shortest)
print(len(shortest))
