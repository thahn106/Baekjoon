N = int(input())
counts = []
for i in range(3):
    counts.append([0]*101)
grid = []
for i in range(N):
    row = list(map(int,input().split()))
    for i,c in enumerate(row):
        counts[i][c] += 1
    grid.append(row)

for row in grid:
    score = 0
    for i,c in enumerate(row):
        if counts[i][c]==1:
            score += c
    print(score)
