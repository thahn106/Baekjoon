N = int(input())
ver = [[False]*N for i in range(N)]
hor = [[False]*N for i in range(N)]
x,y = 0,0
s = input()
for c in s:
    if c == "D":
        nx,ny = x+1,y
        v = True
    elif c == "U":
        nx,ny = x-1,y
        v = True
    elif c == "R":
        nx,ny = x,y+1
        v = False
    else:
        nx,ny = x,y-1
        v = False
    if (0<=nx<N) and  (0<=ny<N):
        if v:
            ver[x][y] = True
            ver[nx][ny] = True
        else:
            hor[x][y] = True
            hor[nx][ny] = True
        x,y = nx,ny

for i in range(N):
    row = ""
    for j in range(N):
        if ver[i][j]:
            if hor[i][j]:
                row+='+'
            else:
                row+='|'
        else:
            if hor[i][j]:
                row+='-'
            else:
                row+='.'
    print(row)
