N,M = map(int,input().split())
A = [list(map(int,input().split())) for n in range(N)]
M,K = map(int,input().split())
B = [list(map(int,input().split())) for n in range(M)]
for n in range(N):
    row = []
    for k in range(K):
        temp = 0
        for m in range(M):
            temp += A[n][m]*B[m][k]
        row.append(temp)
    print(*row)
