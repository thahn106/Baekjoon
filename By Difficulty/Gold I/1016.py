from math import sqrt, floor
mi,ma = map(int,input().split())

primes = [2,3,5,7,11,13,17,19]
for n in range(21, floor(sqrt(ma))+1,2):
    prime = True
    for p in primes:
        if p > sqrt(n):
            break
        if n%p == 0:
            prime = False
            break
    if prime:
        primes.append(n)

r = range(mi,ma+1)
good = [1 for i in r]
for p in primes:
    p2 = p*p
    i = mi//p2
    s = i*p2
    if s < mi:
        s += p2
    while s<=ma:
        good[s-mi]=0
        s+=p2
print(sum(good))
