A, B, N = map(int, input().split())
ans = []
for i in range(N):
    ans.append(A*N+B*(i+1))
print(*ans)
