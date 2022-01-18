import sys
input = sys.stdin.buffer.readline
from bisect import bisect_left

K,L = map(int,input().split())

from math import sqrt

MAXP = L+1

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

found = False
for p in primes:
    if K%p == 0 and p<L:
        found = True
        print("BAD {}".format(p))
        break

if not found:
    print("GOOD")
