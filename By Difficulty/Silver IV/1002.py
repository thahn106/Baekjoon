from math import sqrt
for t in range(int(input())):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    d = sqrt((x1-x2)**2+(y1-y2)**2)
    if d==0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if (r1+r2) < d or (r1+d)<r2 or (r2+d)<r1:
            print(0)
        elif (r1+r2) == d or (r1+d)==r2 or (r2+d)==r1:
            print(1)
        else:
            print(2)
