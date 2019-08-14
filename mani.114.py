mani=int(input())
n=input()
o=["a","e","i","o","u","A","E","I","O","U"]
f=""
for i in n:
	if i not in o:
		f=f+i
print(f[::-1])
