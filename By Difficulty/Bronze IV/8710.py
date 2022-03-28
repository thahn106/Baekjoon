from math import ceil
k,w,m = map(int,input().split())
print(max(0,ceil((w-k)/m)))
