X,Y,W,S = map(int,input().split())
Y,X = min(X,Y), max(X,Y)
if S >= 2*W:
    ans = (X+Y)*W
elif 2*W>S>W:
    ans = (X-Y)*W+Y*S
else:
    ans = 2*((X-Y)//2)*S+Y*S
    if (X-Y)%2:
        ans += W
print(ans)
