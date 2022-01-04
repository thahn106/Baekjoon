from math import floor, ceil
X,Y = map(int,input().split())
Z  = floor(Y*100/X)
if Z >= 99:
    print(-1)
else:
    start =0
    end = X
    while start != end:
        mid = (start+end)//2
        if floor(((Y+mid)/(X+mid))*100)>Z:
            end = mid
        else:
            start = mid+1
    print(start)
