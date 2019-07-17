m1,n1=map(int,input().split())
count1=0
arr=list(map(int,input().split()))[:m1]
for j in arr:
  if j==n1:
    count1+=1
if(count1!=0):
  print("yes")
else:
  print("no")
