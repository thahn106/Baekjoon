from math import sqrt
def dis(x1,y1,x2,y2):
    return sqrt((x1-x2)**2 +(y1-y2)**2)

xa,ya,xb,yb,xc,yc = map(int,input().split())
if (yb-ya)*(xc-xa)==(yc-ya)*(xb-xa):
    ans = float(-1)
else:
    a = dis(xb,yb,xc,yc)
    b = dis(xa,ya,xc,yc)
    c = dis(xb,yb,xa,ya)
    ans = float(2*(max(a,b,c)-min(a,b,c)))
print(ans)
