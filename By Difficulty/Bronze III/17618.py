N = int(input())
ans = 0
for i in range(1,N+1):
    d = sum(list(map(int,list(str(i)))))
    if i%d==0:
        ans += 1
print(ans)
