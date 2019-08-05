mani=int(input())
if mani>1:
    for i in range(2,mani):
        if(mani%i)==0:
            print("yes")
            break
    else:
        print("no")
