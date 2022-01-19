def p2n(st):
    x = ord(st[0])-65
    y = int(st[1])-1
    return x,y

visited = [[False for i in range(6)] for j in range(6)]

x0,y0 = p2n(input())
visited[x0][y0]=True
xp,yp = x0,y0
valid = True
for move in range(35):
    x,y = p2n(input())
    if visited[x][y]:
        valid = False
    visited[x][y] = True
    if not ((abs(x-xp)==2 and abs(y-yp)==1) or (abs(x-xp)==1 and abs(y-yp)==2)):
        valid = False
    xp,yp = x,y

x,y = x0,y0
if not ((abs(x-xp)==2 and abs(y-yp)==1) or (abs(x-xp)==1 and abs(y-yp)==2)):
    valid = False

if valid: print("Valid")
else: print("Invalid")
