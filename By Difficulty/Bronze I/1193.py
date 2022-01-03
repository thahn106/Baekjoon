from math import sqrt,floor
X = int(input())
N = floor(sqrt(2*X))
while N*(N+1) >= 2*X:
    N-=1
X -= N*(N+1)//2
N +=1
q,r = N+1-(X),(X)
if not N % 2:
    q,r = r,q
print("{}/{}".format(q,r))
