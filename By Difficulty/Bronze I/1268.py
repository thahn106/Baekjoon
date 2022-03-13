N = int(input())
grid = []
for i in range(N):
    grid.append(list(map(int,input().split())))

counts = [[0]*N for i in range(N)]

for x in range(N-1):
    for y in range(x+1,N):
        same = False
        for i in range(5):
            if grid[x][i] == grid[y][i]:
                same = True
                break
        if same:
            counts[x][y]=1
            counts[y][x]=1

dup =[sum(counts[s]) for s in range(N)]
cm = -1
ans = -1
for s in range(N):
    if dup[s]>cm:
        cm = dup[s]
        ans = s
print(ans+1)
