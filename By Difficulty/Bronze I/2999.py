from math import isqrt
s = input()
n = len(s)
R = 1
C = n
for i in range(2, isqrt(n)+1):
    if n % i == 0 and i*i <= n:
        R = i
        C = n//i
print("".join(["".join([s[r+c*R] for c in range(C)]) for r in range(R)]))
