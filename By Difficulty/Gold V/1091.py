from math import e, ceil, exp

N = int(input())
P = list(map(int,input().split()))
S = list(map(int,input().split()))
cur = [i for i in range(N)]

ans = 0
while True:
    found = True
    for i in range(N):
        if cur[i]%3 != P[i]:
            found = False
    if found:
        print(ans)
        break
        
    ans += 1
    allsame = True
    for i in range(N):
        cur[i] = S[cur[i]]
        if cur[i] !=i:
            allsame = False
    if allsame:
        print(-1)
        break
