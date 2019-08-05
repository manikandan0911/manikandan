n=list(input())
m=[]
for i in n:
    if i not in m:
        m.append(i)
if(n==m):
    print("Yes")
else:
    print("No")
