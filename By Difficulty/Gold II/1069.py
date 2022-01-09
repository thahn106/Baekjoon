from math import sqrt,ceil
X, Y, D, T = map(int,input().split())

dis = sqrt(X**2+Y**2)

if D/T <1:
    print(float(dis))
else:
    if dis < D:
        print(min(dis, T + D-dis, 2*T))
    else:
        r = ceil(dis/D)
        print(float(min(T*r, T*(r-1)+ dis-D*(r-1))))
