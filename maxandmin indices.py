n=map(int,input().split())
c=[str(i) for i in input().split()]
d=min(c)
e=max(c)
print((c.index(d)+1),(c.index(e)+1))
