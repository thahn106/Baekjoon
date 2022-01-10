import sys
input = sys.stdin.buffer.readline

from bisect import bisect_left, bisect_right

N,M,K = map(int,input().split())
raw =  [int(input()) for i in range(N)]
dp = [0 for i in range(N+1)]

sum = 0
for i in range(N):
    sum+=raw[i]
    dp[i+1]=sum

mods = []

MV = 2**64

for c in range(M+K):
    a,b,c = map(int,input().split())
    if a == 1:
        pair = (b,c-raw[b-1])
        raw[b-1] = c
        mods.insert(bisect_left(mods,pair),pair)
        # print(mods)
    elif a==2:
        m = 0
        i = bisect_left(mods,(b,-MV))
        while i <len(mods)  and mods[i][0]<=c:
            m+=mods[i][1]
            i+=1
        print(dp[c]-dp[b-1]+m)
