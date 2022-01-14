import sys
input = sys.stdin.buffer.readline

N,M = map(int,input().split())
a = list(map(int,input().split()))
dp = [0]
sum = 0
for i in a:
    sum+=i
    dp.append(sum)

for m in range(M):
    a,b = map(int,input().split())
    sys.stdout.write(str(dp[b]-dp[a-1])+"\n")
sys.stdout.flush()
