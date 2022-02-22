from math import gcd

N,M = map(int,input().split())
d = gcd(N,M)
N = N//d
M = M//d
print((M-1)*d)
