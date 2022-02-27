N,T = map(int,input().split())

ans = 10**9
found = False
for n in range(N):
    s,i,c = map(int,input().split())
    for k in range(c):
        cur = s+k*i
        if cur >= T:
            found = True
            ans = min(ans, cur)

if found:
    print(ans-T)
else:
    print(-1)
