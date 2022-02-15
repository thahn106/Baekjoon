from math import sqrt, ceil
N = int(input())

MAXP = ceil(sqrt(N))
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

for p in primes:
    n,r = divmod(N,p)
    while not r:
        print(p)
        N = n
        n,r = divmod(N,p)
    if N == 1:
        break
if N>1:
    print(N)
