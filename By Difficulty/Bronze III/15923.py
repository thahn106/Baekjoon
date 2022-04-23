N = int(input())
X, Y = map(int,input().split())
x, y = X, Y
ans = 0
for i in range(N-1):
    a, b = map(int,input().split())
    ans += abs(a-x)+abs(b-y)
    x, y = a, b

ans += abs(X-x)+abs(Y-y)
print(ans)
