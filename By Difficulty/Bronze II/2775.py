from math import comb
for t in range(int(input())):
    k = int(input())
    n = int(input())
    print(comb(n+k,k+1))
