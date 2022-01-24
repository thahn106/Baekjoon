from math import pi
N = 1
M = 12*5280
d,r,t = map(float,input().split())
while r:
    D = d*pi*r
    print("Trip #{}: {:.2f} {:.2f}".format(N, D/M, (D*3600/(M*t))))
    N+=1
    d,r,t = map(float,input().split())
