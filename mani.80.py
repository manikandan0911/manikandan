m=input()
n=[]
for i in range(0,len(m)):
        if(int(m[i])%2==1):
           n.append(m[i])
print(*n,end="")
