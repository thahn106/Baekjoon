N,M = map(int,input().split())
grid = [input() for i in range(N)]
board = 0
for i in range(N):
    row = grid[i]
    run = 0
    for c in row:
        if c == '-':
            run = 1
        elif run:
            run =0
            board+=1
    if run:
        board+=1
for i in range(M):
    row =  [r[i] for r in grid]
    run = 0
    for c in row:
        if c == '|':
            run = 1
        elif run:
            run = 0
            board +=1
    if run:
        board+=1

print(board)
