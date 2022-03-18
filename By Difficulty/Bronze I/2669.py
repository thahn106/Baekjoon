grid = [[0]*100 for i in range(100)]
for i in range(4):
    a,b,c,d = map(int,input().split())
    for x in range(a,c):
        for y in range(b,d):
            grid[x][y]=1
ans = 0
for row in grid:
    ans += sum(row)
print(ans)
