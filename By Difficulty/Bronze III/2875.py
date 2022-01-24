from math import ceil
N,M,K = map(int,input().split())
m = min(N//2,M)
K -= N-2*m + M-m
if K>0:
    m -= ceil(K/3)
print(m)
