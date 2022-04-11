from math import ceil

N, K = map(int, input().split())
grid = [[0 for g in range(2)] for i in range(6)]
for n in range(N):
    a, b = map(int, input().split())
    grid[b-1][a] += 1

ans = 0
ans += ceil((grid[0][0]+grid[1][0]+grid[0][1]+grid[1][1])/K)
for i in range(1, 3):
    ans += ceil((grid[2*i][0]+grid[2*i+1][0])/K)
    ans += ceil((grid[2*i][1]+grid[2*i+1][1])/K)
print(ans)
