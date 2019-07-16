mani,nivi=map(int,input().split())
for i in range(mani+1,nivi):
    s=0
    a=i
    while(a>0):
        c=a%10
        s+=c*c*c
        a//=10
    if(i==s):
      print(i,end=" ")
