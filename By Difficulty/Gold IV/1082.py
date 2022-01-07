def l2n(l):
    return int("".join(l))

N = int(input())
P = list(map(int,input().split()))
M = int(input())

dp = [-1 for m in range(M+1)]
for n in range(N):
    if P[n]<=M:
        dp[P[n]] = max(n,dp[P[n]])
# print(dp)
for i in range(M):
    if dp[i] != -1:
        for n in range(N):
            if i+P[n]<=M:
                # print("i:{} P[n]:{} n:{}".format(i,P[n],n))
                num = [c for c in str(dp[i])] + [str(n)]
                # print(num)
                num.sort(reverse=True)
                num = l2n(num)
                dp[P[n]+i] = max(num,dp[P[n]+i])
    # print("i:{} dp[i]:{}".format(i,dp[i]))
print(max(dp))
