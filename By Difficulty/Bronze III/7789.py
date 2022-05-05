A, B = map(int, input().split())
C = B*1000000+A
primes = (A%2 and C%2)

if primes:
    for i in range(3,10000,2):
        if A%i == 0 or  C%i == 0:
            primes = False
            break
if primes:
    print("Yes")
else:
    print("No")
