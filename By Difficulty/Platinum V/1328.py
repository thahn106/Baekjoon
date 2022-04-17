N,L,R = map(int,input().split())

dp = [[[0 for k in range(101)]for j in range(101)] for i in range(101)]
dp[1][1][1] = 1

for i in range(2,N+1):
    for j in range(1,L+1):
        for k in range(1,R+1):
            dp[i][j][k] = (dp[i-1][j][k]*(i-2)+dp[i-1][j][k-1]+dp[i-1][j-1][k]) % 1000000007
print(dp[N][L][R])
