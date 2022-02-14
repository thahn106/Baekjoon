n,T = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
for i in range(n):
    if T >= a[i]:
        ans+=1
        T -= a[i]
    else:
        break
print(ans)
