z=int(input())
v=list(map(int,input().split()))[0:z]
v.sort(reverse=False)
i=0
while i<z:
    print(v[i],end=" ")
    i+=1
  
