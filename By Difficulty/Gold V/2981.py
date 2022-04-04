from math import gcd, sqrt
N = int(input())
M = [int(input()) for i in range(N)]
d = [i-M[0] for i in M[1:]]
g = gcd(*d)

ans = []
for i in range(1,int(sqrt(g))+1):
    if g%i == 0:
        ans.append(i)
        if i*i !=g:
            ans.append(g//i)

ans.sort()
print(*ans[1:])
