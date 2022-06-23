from math import isqrt, gcd
G,L = map(int,input().split())
T = L//G
A = 1
B = T
for a in range(1,isqrt(T)+1):
    b,r = divmod(T,a)
    if not r:
        if gcd(a,b)==1:
            if a+b<A+B:
                A=a
                B=b

print(A*G,B*G)
