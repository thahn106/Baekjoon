from math import sqrt,floor
N = int(input())

# primes = [2]
primes = [2,3,5,7,11,13,17,19]
ans = N
for p in primes:
    if not N%p:
        ans = (ans*(p-1))//p
        while not N%p:
            N = N//p

for n in range(23, floor(sqrt(N))+1,2):
    prime = True
    for p in primes:
        if p > sqrt(n):
            break
        if n%p == 0:
            prime = False
            break
    if prime:
        p=n
        if not N%p:
            ans = (ans*(p-1))//p
            while not N%p:
                N = N // p
        primes.append(n)
        if n > floor(sqrt(N))+1:
            break
if N>1:
    ans = (ans*(N-1))//N
print(ans)
