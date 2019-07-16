M1,R1=map(int,input().split())
arrq=[]
j=M1
m=1
arrq=[int(i)for i in input().split()]
sum=0
i=0
while R1>0:
  sum+=arrq[i]
  R1=R1-1
  i=i+1
print(sum)
