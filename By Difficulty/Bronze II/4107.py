N,M,K = map(int,input().split())

while N or M or K:
    k = list(map(int,input().split()))
    ans = N
    cur = N
    for m in range(M-1):
        cur += k[m%K]
        ans += cur
    print(ans)

    N,M,K = map(int,input().split())
