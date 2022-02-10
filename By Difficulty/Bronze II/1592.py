N,M,L = map(int,input().split())
counts = [0 for i in range(N)]
cur = 0
counts[cur]=1
ans = 0
while counts[cur]<M:
    if counts[cur]%2:
        cur = (cur+L)%N
    else:
        cur = (cur-L)%N
    counts[cur]+=1
    ans += 1
print(ans)
