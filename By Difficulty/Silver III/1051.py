N,M = map(int,input().split())
matrix = []
for i in range(N):
    row = input()
    matrix.append(row)

ans = 0
for i in range(N):
    for j in range(M):
        base  = matrix[i][j]
        for k in range(0, min(N-i,M-j)):
            if base == matrix[i][j+k] and base == matrix[i+k][j+k] and base == matrix[i+k][j]:
                ans = max(ans, (k+1)*(k+1))
print(ans)
