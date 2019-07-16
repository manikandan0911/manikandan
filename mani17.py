m99=int(input())
sum=0
n=m99
while n>0:
  digit=n%10
  sum+=digit**3
  n//=10
if m99==sum:
  print("yes")
else:
  print("no")
