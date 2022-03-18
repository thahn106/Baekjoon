N = int(input())
a = list(range(1, N+1))
ans = []
for i in range(N):
    ans.append(a.pop(0))
    if a:
        a.append(a.pop(0))
print(*ans)
