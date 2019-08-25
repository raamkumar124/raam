A,B,C=list(map(int,input().split()))
if (A + B >= C) or (A + C >= B) or (B + C >= A) :
  print("yes")
else:
  print("no")
