number1=int(input())
for i in range(number1):
  num=list(map(int,input().split()))
  a=min(num)
  b=max(num)
  print(a,b)
