from math import comb
N,M,K = map(int,input().split())

num = 0
for k in range(K,M+1):
    num+= comb(M,k)*comb(N-M,M-k)

denom = comb(N,M)
print(num/denom)
