from bisect import bisect_right
from math import sqrt

MAXP = 130000*2
primes = [2,3,5,7,11,13,17,19]
for n in range(21, MAXP, 2):
    prime = True
    for p in primes:
        if p > sqrt(n):
            break
        if n % p == 0:
            prime = False
            break
    if prime:
        primes.append(n)

n = int(input())
while n:
    a = bisect_right(primes, n)
    b = bisect_right(primes, 2*n)
    print(b-a)
    n = int(input())
