N, X = map(int,input().split())
ans = []
for i in list(map(int,input().split())):
    if i<X:
        ans.append(i)
print(*ans)
