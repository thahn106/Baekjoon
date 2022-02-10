from math import sqrt, floor

N = int(input())
ans = 0
while N:
    d = floor(sqrt(2*N))
    if d*(d+1)//2>N:
        d-=1
    N -= d*(d+1)//2
    ans +=d
print(ans)
