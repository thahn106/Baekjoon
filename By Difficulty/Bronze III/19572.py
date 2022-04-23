d = list(map(int, input().split()))
D = sum(d)/2
ans = []
for i in d:
    ans.append(D-i)
if min(ans)<=0:
    print(-1)
else:
    print(1)
    print(*ans[::-1])
