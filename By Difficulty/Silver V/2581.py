from math import sqrt
from bisect import bisect_left, bisect_right
MAXP = 10000
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

M = int(input())
N = int(input())

m = bisect_left(primes, M)
n = bisect_right(primes, N)
p = primes[m:n]
if p:
    print(sum(p))
    print(p[0])
else:
    print(-1)
