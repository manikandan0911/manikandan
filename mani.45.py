mani1=int(input())
sum=0
if mani1>0:
  digit=mani1%10
  sum+=digit
  mani1=mani1//10
print(sum)
