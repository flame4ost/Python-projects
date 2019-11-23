input_string = input()
splitter = input_string.split()
final = []
for i in range(0, len(splitter)):
    for j in range(0, len(splitter[i])):
        if(j==0):
            final.append(splitter[i][j].upper())
        else:
            final.append(splitter[i][j])
    final.append(' ')
count = input_string.count(' ')
print(''.join(final))
print (count)
