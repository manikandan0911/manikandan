mani=int(input())
if mani>1:
    for i in range(1,mani+1):
        if(mani%i)==0:
            print(i,end=" ")
