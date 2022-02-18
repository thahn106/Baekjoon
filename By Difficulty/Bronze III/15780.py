N,K = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
for i in a:
    ans += (i+1)//2

if N<=ans:
    print("YES")
else:
    print("NO")
