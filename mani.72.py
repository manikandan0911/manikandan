mr=input()
flag=0
ab=list('aeiouAEIOU')
for i in mr:
    if i in ab:
        print("yes")
        flag=1
        break
if flag==0:
    print("no")
