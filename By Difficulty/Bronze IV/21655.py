n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(input())
input()
b = []
for i in range(n):
    b.append(input())
ans = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == b[i][j]:
            ans += 1
print(ans)
