N, L, K = map(int, input().split())

E, H = 0, 0

for i in range(N):
    e, h = map(int,input().split())
    if h <= L:
        H += 1
    elif e <= L:
        E += 1

ans = min(K,H)*140
K -= min(K,H)
ans += min(K,E)*100
print(ans)
