N = int(input())
stairs = []
for i in range(N):
    stairs.append(int(input()))
dp = [[0,0] for i in range(N+1)]
for i in range(N):
    if i != 0:
        dp[i+1][1] = max(dp[i-1])+stairs[i]
    if i == 1:
        dp[i+1][0] = max(dp[i])+stairs[i]
    else:
        dp[i+1][0] = dp[i][1]+stairs[i]

print(max(dp[N]))
