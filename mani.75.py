m=input()
n=len(m)
if n%2!=0:
    m=m[:int(n/2)]+'*'+m[int(n/2)+1:n]
else:
    m=m[:int(n/2)-1]+'**'+m[int(n/2)+1:n]
print(m)
