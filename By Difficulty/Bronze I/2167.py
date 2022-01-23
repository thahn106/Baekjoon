N,M = map(int,input().split())
dp = [[0 for i in range(M+1)]]
for i in range(N):
    row = list(map(int,input().split()))
    dr = [0]
    rr = 0
    for i in range(M):
        rr+=row[i]
        dr.append(dp[-1][i+1]+rr)
    dp.append(dr)

for k in range(int(input())):
    i,j,x,y = map(int,input().split())
    print(dp[x][y]+dp[i-1][j-1]-dp[x][j-1]-dp[i-1][y])
