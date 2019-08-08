m,n=map(str,input().split(" "))
count=0
for i in range(0,len(m)):
	if m[i]!=n[i]:
		count=count+1
if count>1:
	print("no")
else:
	print("yes")
