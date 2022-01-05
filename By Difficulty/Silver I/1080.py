N,M = map(int,input().split())
A = []
B = []
for i in range(N):
    A.append([int(c) for c in input()])
for i in range(N):
    B.append([int(c) for c in input()])
ans = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j]!=B[i][j]:
            for i2 in range(i,i+3):
                for j2 in range(j,j+3):
                    A[i2][j2]=1-A[i2][j2]
            ans+=1
same = True
for i in range(N):
    for j in range(M):
        if A[i][j]!=B[i][j]:
            same=False

if same:
    print(ans)
else:
    print(-1)
