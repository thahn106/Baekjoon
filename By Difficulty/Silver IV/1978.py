MAXP = 1000
from math import sqrt
from bisect import bisect_left
primes = [2,3,5,7,11,13,17,19]
for n in range(21, MAXP,2):
    prime = True
    for p in primes:
        if p > sqrt(n):
            break
        if n%p == 0:
            prime = False
            break
    if prime:
        primes.append(n)

N = int(input())
a = list(map(int,input().split()))

ans=0
for n in a:
    i = bisect_left(primes,n)
    if i<len(primes) and primes[i] == n:
        ans+=1

print(ans)
