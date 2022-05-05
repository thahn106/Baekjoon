from math import sqrt

def v(c):
    if ord(c)>96:
        return ord(c)-96
    else:
        return ord(c)-64+26

MAXP = 10001
primes = [2,3,5,7,11,13,17,19]
for n in range(21, MAXP+1,2):
    prime = True
    for p in primes:
        if p > sqrt(n):
            break
        if n%p == 0:
            prime = False
            break
    if prime:
        primes.append(n)
primes.append(1)

s = input()
ans = 0
for c in s:
    ans += v(c)
if ans in primes:
    print("It is a prime word.")
else:
    print("It is not a prime word.")
