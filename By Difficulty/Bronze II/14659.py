N = int(input())
H = list(map(int,input().split()))

maxc = 0
curh = 0
curk = 0
for i,h in enumerate(H):
    if h>curh:
        maxc = max(maxc, curk)
        curh = h
        curk = 0
    else:
        curk += 1

maxc = max(maxc, curk)
print(maxc)
