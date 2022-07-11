n = int(input())
s = input().split()
a = s[0][0]
ans = 1
for i in s:
    if i[0]!=a:
        ans = 0
print(ans)
