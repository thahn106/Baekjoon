N = int(input())
grid = [list(map(int,input().split())) for i in range(N)]

phase = N*N
def work(x,y, size):
    ng = sum([sum(row[x:x+size]) for row in grid[y:y+size]])
    if ng ==0:
        return 1,0
    elif ng == size*size:
        return 0,1
    else:
        ns = size//2
        a = 0
        b = 0
        for i in range(2):
            for j in range(2):
                ai,bi = work(x+ns*i,y+ns*j,ns)
                a+=ai
                b+=bi
        return a,b

x,y = work(0,0,N)
print(x)
print(y)
