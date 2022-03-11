grid = [input() for i in range(5)]
l = max(list(map(len,grid)))
ans = ""
for i in range(l):
    for j in range(5):
        if i< len(grid[j]):
            ans += grid[j][i]
print(ans)
