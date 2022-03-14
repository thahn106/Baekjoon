N = int(input())
grid =[input() for i in range(N)]

ans = 0
for i in range(N):
    cur = 0
    for j in range(N):
        if grid[i][j]=='X':
            if cur >=2:
                ans += 1
            cur = 0
        else:
            cur +=1
    if cur>=2:
        ans += 1

vans = 0
for i in range(N):
    cur = 0
    for j in range(N):
        if grid[j][i]=='X':
            if cur >=2:
                vans += 1
            cur = 0
        else:
            cur +=1
    if cur>=2:
        vans += 1
print(ans, vans)
