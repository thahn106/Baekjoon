N = int(input())
a = list(map(int,input().split()))
dp = [0 for i in range(N)]

for i in range(N):
    ans = 0
    for j in range(i):
        if a[j]<a[i]:
            ans = max(ans,dp[j])
    dp[i] = ans+1
print(max(dp))
