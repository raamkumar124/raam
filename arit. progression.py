def sumOfAP(N,A,D):
  sum=(N/2)*(2*A+(N-1)*D)
  return sum
N,A,D=map(int,input().split())
print(int(sumOfAP(N,A,D)))
