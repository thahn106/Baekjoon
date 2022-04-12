A,B,C,M = map(int,input().split())
t = 0
ans = 0
for i in range(24):
    if t+A<=M:
        t +=A
        ans += B
    else:
        t = max(0,t-C)
print(ans)
