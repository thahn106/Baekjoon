from math import floor
A,B,N =map(int,input().split())

d,r = divmod(A,B)
for i in range(N):
    r*=10
    d,r = divmod(r,B)
print(d)
