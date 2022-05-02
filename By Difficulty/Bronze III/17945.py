from math import sqrt
A, B = map(int, input().split())
D = int(sqrt(A*A-B))
if D == 0:
    print(-A)
else:
    print(-A-D, -A+D)
