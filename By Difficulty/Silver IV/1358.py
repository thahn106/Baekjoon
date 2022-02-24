W,H,X,Y,P = map(int,input().split())
r = H//2

ans = 0
for p in range(P):
    x,y = map(int,input().split())
    if x<X:
        if (X-x)**2+(Y+r-y)**2<=r**2:
            ans+=1
    elif X<=x<=X+W:
        if Y<=y<=Y+H:
            ans+=1
    else:
        if (X+W-x)**2+(Y+r-y)**2<=r**2:
            ans+=1
print(ans)
