from math import sqrt, floor
for t in range(int(input())):
    x,y = map(int,input().split())
    D = y-x
    n = floor(sqrt(D))
    R = D -n*n
    if R == 0:
        print(2*n-1)
    elif R<=n:
        print(2*n)
    else:
        print(2*n +1)
