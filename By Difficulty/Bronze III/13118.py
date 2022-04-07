p = list(map(int,input().split()))
x,y,r = map(int,input().split())
ans = 0
for i,c in enumerate(p):
    if c==x:
        ans = i+1
print(ans)
