mani=int(input())
s=list(map(int,input().split()))
o=sorted(l)
r=[]
for i in o:
    r.append(s.index(i)+1)
print(*r)
