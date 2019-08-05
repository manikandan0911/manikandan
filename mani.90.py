m=input()
p=[]
for i in m:
    if(i.isnumeric()):
        p.append(i)
print(''.join(p))
