from math import sqrt

N = int(input())

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

cur = [2,3,5,7]
for i in range(N-1):
    last = cur
    cur = []
    for prev in last:
        for d in [1,3,7,9]:
            n = prev*10+d
            prime = True
            for p in primes[1:]:
                if p>sqrt(n):
                    break
                else:
                    if n%p==0:
                        prime=False
                        break
            if prime:
                cur.append(n)
for p in cur:
    print(p)
