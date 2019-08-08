mani=int(input())
f=1
i=0
for i in range(mani,0,-1):
    f=f*i
if mani==0:
    print("1")
else:
    print(f)
