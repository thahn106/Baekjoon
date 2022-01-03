from math import comb
for t in range(int(input())):
    n,m = map(int,input().split())
    print(comb(m,n))
