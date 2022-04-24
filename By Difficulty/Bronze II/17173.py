N, M = map(int, input().split())
K = list(map(int, input().split()))

ans = 0
for i in range(1, N+1):
    for k in K:
        if i % k == 0:
            ans += i
            break
print(ans)
