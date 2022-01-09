from itertools import combinations
from math import sqrt

for t in range(int(input())):
    N = int(input())
    x = []
    y = []
    for n in range(N):
        u,v = map(int,input().split())
        x.append(u)
        y.append(v)
    SX = sum(x)
    SY = sum(y)
    ans = float(40000000)
    for subset in combinations(range(N),N//2):
        sx = 0
        sy = 0
        for i in subset:
            sx+=x[i]
            sy+=y[i]
        ex=SX-sx
        ey=SY-sy
        ans = min(ans, sqrt((ex-sx)**2+(ey-sy)**2))
    print(ans)
