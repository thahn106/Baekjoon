from math import sqrt
from bisect import bisect_left, bisect_right

M,N = map(int,input().split())
primes = [2,3,5,7,11,13,17,19]
for n in range(21, N+1,2):
    prime = True
    for p in primes:
        if p > sqrt(n):
            break
        if n%p == 0:
            prime = False
            break
    if prime:
        primes.append(n)

for p in primes[bisect_left(primes,M):bisect_right(primes,N)]:
    print(p)
