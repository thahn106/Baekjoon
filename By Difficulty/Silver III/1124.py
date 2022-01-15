import sys
input = sys.stdin.buffer.readline
from bisect import bisect_left

from math import sqrt
a,b = map(int,input().split())
primes = [2,3]
dp = [0,0,1,1,2]
for n in range(5, b+1):
    prime = True
    for p in primes:
        if p > sqrt(n):
            break
        if n%p == 0:
            dp.append(dp[n//p]+1)
            prime = False
            break
    if prime:
        dp.append(1)
        primes.append(n)

ans = 0
for i in range(a,b+1):
    c = dp[i]
    if primes[bisect_left(primes,c)] == c:
        ans +=1
print(ans)
