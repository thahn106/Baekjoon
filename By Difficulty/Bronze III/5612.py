n = int(input())
m = int(input())

ans = True
ma = m
for i in range(n):
    a,b = map(int,input().split())
    m += (a-b)
    ma = max(ma, m)
    if m<0:
        ans = False
if ans:
    print(ma)
else:
    print(0)
