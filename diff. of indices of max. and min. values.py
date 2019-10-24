n=int(input())
c=list(map(int,input().split()))[:n]
d=min(c)
e=max(c)
print((c.index(e)+1)-(c.index(d)+1))
