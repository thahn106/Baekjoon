N,L = map(int,input().split())
ans = 101
a=0
for k in range(L,101):
    ak = N - k*(k-1)//2
    if ak%k == 0  and ak//k >=0:
        if ans == 101:
            a = ak//k
        ans = min(k,ans)
if ans == 101:
    print(-1)
else:
    anslist = [a+i for i in range(ans)]
    print(*anslist)
