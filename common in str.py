n=int(input())
a=[]
for i in range(0,n):
  log=input()
  a.append(log)
v=[]
for i in zip(*a):
  if(i.count(i[0])==len(i)):
    v.append(i[0])
  else:
    break
print(''.join(v))
