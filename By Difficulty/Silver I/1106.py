C,N = map(int,input().split())
cities = []
for i in range(N):
    a,b = map(int,input().split())
    cities.append((a,b))

dp = [-1 for i in range(C+100)]
dp[0]=0

for i in range(C):
    if dp[i] != -1:
        for a,b in cities:
            if dp[i+b] == -1:
                dp[i+b] = dp[i]+a
            else:
                dp[i+b] = min(dp[i]+a,dp[i+b])
                
ans = max(dp)
for i in range(C,C+100):
    if dp[i]!=-1:
        ans = min(ans,dp[i])
print(ans)
