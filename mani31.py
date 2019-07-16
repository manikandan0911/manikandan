#a
a11=list(input())
b11=" "
for i in range(len(a11)):
    if b11 in a11:
        a11.remove(b11)
print(len(a11))
