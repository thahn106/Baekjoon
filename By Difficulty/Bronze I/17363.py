f = {
    '.': '.',
    'O': 'O',
    '-': '|',
    '|': '-',
    '/': '\\',
    '\\': '/',
    '^': '<',
    '<': 'v',
    'v': '>',
    '>': '^'
}
R, C = map(int, input().split())
grid = []
for r in range(R):
    grid.append(input())
for c in range(C):
    row = ""
    for r in range(R):
        row += f[grid[r][C-1-c]]
    print(row)
