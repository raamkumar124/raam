n=input()
a=[]
for i in n:
  if i not in a:
    a.append(i)
if len(a)==3:
  print('Wonder')
else:
   print('-1')     
