N = int(input())
grid = [list(map(int,input().split())) for i in range(N)]

phase = N*N
def work(x,y, size):
    ng = sum([sum(row[x:x+size]) for row in grid[y:y+size]])
    asu = sum([sum([abs(c) for c in row[x:x+size]]) for row in grid[y:y+size]])
    if ng == -size*size:
        return 1,0,0
    elif asu == 0:
        return 0,1,0
    elif ng == size*size:
        return 0,0,1
    else:
        ns = size//3
        a = 0
        b = 0
        c = 0
        for i in range(3):
            for j in range(3):
                ai,bi,ci = work(x+ns*i,y+ns*j,ns)
                a+=ai
                b+=bi
                c+=ci
        return a,b,c

x,y,z = work(0,0,N)
print(x)
print(y)
print(z)
