W, N, P = map(int, input().split())
ans = 0
for i in list(map(int, input().split())):
    if W <= i <= N:
        ans += 1
print(ans)
