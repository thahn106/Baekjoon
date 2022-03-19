N,M = map(int,input().split())
A = [list(map(int,input().split())) for i in range(N)]
B = [list(map(int,input().split())) for i in range(N)]
for i in range(N):
    row = []
    for j in range(M):
        row.append(A[i][j]+B[i][j])
    print(*row)
