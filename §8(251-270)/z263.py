s=input("введите строку= ").split()
s1=' '
for i in range(len(s)):
  if s[i:i+5]=="child":
      r='children'
      s1=s1+r
      i=i+1
  else:
      s1=s1+s[i]
 
print(' '.join(['children' if i == 'child' else i for i in s]))
