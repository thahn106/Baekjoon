import sys
mod = 1000000007
dp = [1]*4000001
for i in range(1,4000001):
    dp[i]=dp[i-1]*i % mod

for m in range(int(input())):
    N,K = map(int,sys.stdin.readline().strip().split())
    sys.stdout.write(str(dp[N]*pow(dp[K],-1,mod)*pow(dp[N-K],-1,mod) % mod)+'\n')
sys.stdout.flush()
