m1=input()
count1=0
for r in m1:
  if (r.isdigit() or r.isalpha()):
    count1+=1
if count1!=0:
  print("Yes")
else:
  print("No")
