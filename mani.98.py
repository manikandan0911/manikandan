ntr=int(input())
mani=list(map(int,input().split()))
for y in range(len(mani)-1):
   if(mani[y]>mani[y+1]):
      print(y)
