s=int(input())
x=list(map(int,input().split()))[0:s]
a=sum(x)
if(a%2==0 and a%3==0 and a%5==0):
    print('1')
else:
    print('0')
