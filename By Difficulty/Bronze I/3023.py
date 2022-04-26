grid = []
R, C = map(int, input().split())
for r in range(R):
    grid.append(input())

x, y = map(int, input().split())
x -= 1
y -= 1
for r in range(2*R):
    row = ""
    a = r
    if a>=R:
        a = 2*R-1-r
    for c in range(2*C):
        b = c
        if b>=C:
            b = 2*C-1-c
        ans = grid[a][b]
        if r == x and c == y:
            if ans == '#':
                ans = '.'
            else:
                ans = '#'
        row+=ans
    print(row)
