first = 'GOOD MORNING'
second = 'GOOD BYE'
len1 = len(first)
len2 = len(second)
count = 0
for i in range(len1):
 if i < len2 and first[i] == second[i]:
 count += 1
 continue
 else:
 break
return count
