from math import ceil
N,K = map(int,input().split())
for k in range(K):
    s,t,r = map(int,input().split())
    n = ceil(N/s)
    d = ceil(n/t)
    print(n+(d-1)*r)
