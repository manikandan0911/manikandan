mani=int(input())
s,t=0,1
while mani>0:
  print(t,end=' ')
  s,t=t,s+t
  mani=mani-1
