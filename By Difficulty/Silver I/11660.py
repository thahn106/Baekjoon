import sys
input = sys.stdin.buffer.readline

N,M = map(int,input().split())

run = [[0 for i in range(N+1)]]

for i in range(N):
    row = list(map(int,input().split()))
    rs = 0
    tr = [0]
    for j in range(N):
        rs += row[j]
        tr.append(run[i][j+1]+rs)
    run.append(tr)
    
for i in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    ans = run[x2][y2]-run[x1-1][y2]-run[x2][y1-1]+run[x1-1][y1-1]
    print(ans)
