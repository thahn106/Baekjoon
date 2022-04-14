n = int(input())
grid = [input() for i in range(n)]
K = int(input())
if K == 1:
    for row in grid:
        print(row)
elif K == 2:
    for row in grid:
        print(row[::-1])
else:
    for i in range(n):
        print(grid[n-1-i])
