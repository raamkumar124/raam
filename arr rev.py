n=int(input())
v=list(map(int,input().split()))[0:n]
v.sort(reverse=True)
i=0
while i<n:
    print(v[i],end="\n")
    i+=1
