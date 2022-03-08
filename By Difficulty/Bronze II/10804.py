ans = list(range(1,21))
for i in range(10):
    a,b = map(int,input().split())
    ans = ans[:a-1] +ans[a-1:b][::-1]+ans[b:]
print(*ans)
