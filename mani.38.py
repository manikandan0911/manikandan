ln=list(map(int,input().split()))
a91=ln[0]
b11=ln[1]
a91=a91^b11
b11=a91^b11
a91=a91^b11
print(a91,b11)
