a,b,n,w = map(int,input().split())
g,s=0,0
fail = False
for goats in range(1,n):
    sheep = n-goats
    if w == goats*a+sheep*b:
        if g:
            fail = True
        else:
            g = goats
            s = sheep

if fail or not g:
    print(-1)
else:
    print(g,s)
