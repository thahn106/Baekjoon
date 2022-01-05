N,r,c = map(int,input().split())
ans = 0
for i in range(N):
    if c%2:
        ans+= 4**i
    if r%2:
        ans+= (4**i)*2
    r=r//2
    c=c//2
print(ans)
