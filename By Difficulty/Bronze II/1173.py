N, m, M, T, R = map(int,input().split())
if M-m < T:
    print(-1)
else:
    ans = 0
    cur = m
    while N:
        if cur + T<=M:
            N -= 1
            ans +=1
            cur += T
        else:
            cur = max(m, cur-R)
            ans +=1
    print(ans)
