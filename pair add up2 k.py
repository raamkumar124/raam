n,k=map(int,input().split())
p=list(map(int,input().split()))[:n]
c=0
for i in range(0,len(p)-1):
    for s in range(i+1,len(p)-1):
        if(p[i]+p[s]==k):
            c+=1
if (c==1):
    print("yes")
else:
    print("no")
