from math import comb
N,K = map(int,input().split())
print(comb(N+K-1, (K-1))%1000000000)
