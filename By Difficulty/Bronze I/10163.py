grid = {}
T = int(input())
grid = [[0]*1001 for i in range(1001)]
for t in range(T):
    X,Y,A,B = map(int,input().split())
    for x in range(X, X+A):
        for y in range(Y, Y+B):
            grid[x][y] = t+1

ans = [0]*(T+1)
for x in range(1001):
    for y in range(1001):
        if grid[x][y]:
            ans[grid[x][y]] += 1
for v in ans[1:]:
    print(v)
