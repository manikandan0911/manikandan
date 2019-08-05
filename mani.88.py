import math
m,n=map(int,input().split())
o=math.gcd(m,n)
lcm=(m*n)/o
print(math.ceil(lcm))
