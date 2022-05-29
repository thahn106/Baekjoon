N, M = map(int, input().split())
grid = [[N for j in range(4)] for i in range(M)]

rows = []
for n in range(N):
    row = input()
    rows.append(row)
    for i,c in enumerate(row):
        for j,k in enumerate('ACGT'):
            if c == k:
                ind = j
        grid[i][ind] -= 1

anss = ""
ans = 0
for row in grid:
    temp = N+1
    ind = -1
    for i in range(4):
        if row[i] < temp:
            ind = i
            temp = row[i]
    ans += row[ind]
    anss += 'ACGT'[ind]
print(anss)
print(ans)
