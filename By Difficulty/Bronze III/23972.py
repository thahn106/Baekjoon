from math import ceil
K,N = map(int, input().split())
if N==1:
    print(-1)
else:
    d,r = divmod(N*K,N-1)
    print(d+(r>0))
