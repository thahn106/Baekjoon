N = int(input())

dir = 2
x,y = 0,0
minx,maxx,miny,maxy = 0,0,0,0
ch = [(0,1),(1,0),(0,-1),(-1,0)]

s = {}
s[(0,0)]=True
for c in input():
    if c == 'R':
        dir = (dir+1)%4
    elif c == 'L':
        dir = (dir-1)%4
    else:
        dx,dy = ch[dir]
        x += dx
        y += dy
        s[(x,y)]=True
        minx = min(x,minx)
        maxx = max(x,maxx)
        miny = min(y,miny)
        maxy = max(y,maxy)

for y in range(maxy, miny-1, -1):
    row = ""
    for x in range(minx,maxx+1):
        if (x,y) in s:
            row+="."
        else:
            row+='#'
    print(row)
