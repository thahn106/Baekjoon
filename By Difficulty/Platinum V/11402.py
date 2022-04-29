import sys

N, K, mod = map(int, input().split())
dp = [[-1]*mod for i in range(mod)]


sys.setrecursionlimit(2005)

def binom(n, k):
    if dp[n][k] == -1:
        if n < k:
            dp[n][k] = 0
        elif k == 0 or k == n:
            dp[n][k] = 1
        else:
            dp[n][k] = (binom(n-1, k)+binom(n-1, k-1)) % mod
    return dp[n][k]


ans = 1
while N or K:
    N, n = divmod(N, mod)
    K, k = divmod(K, mod)
    ans = (ans*binom(n, k)) % mod
print(ans)
