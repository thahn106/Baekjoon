N,M = map(int,input().split())
a = list(map(lambda i: int(i)%M,input().split()))
ans = 1
for i in a:
    ans = (ans*i)%M
print(ans)
