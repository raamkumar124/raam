n=int(input())
x=list(map(str,input().split()))[0:n]
a=[]
for num in x:
  if num not in a:
    a.append(num)
print(' '.join(a))    
